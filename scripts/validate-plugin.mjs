#!/usr/bin/env node
// Validador de integridad del plugin Indash Stack.
// Chequea, sin dependencias externas:
//   1. Que los JSON de config parseen y tengan los campos mínimos.
//   2. Que cada SKILL.md tenga frontmatter válido (name + description).
//   3. Que TODA referencia a un archivo/carpeta dentro de un SKILL.md exista.
//   4. Que el hook de SessionStart apunte a un archivo real.
// Uso: node scripts/validate-plugin.mjs   (sale con código 1 si algo falla)

import { readFileSync, existsSync, readdirSync, statSync } from "node:fs";
import { join, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const errors = [];
const ok = [];

const rel = (p) => p.replace(ROOT + "/", "");
const fail = (msg) => errors.push(msg);
const pass = (msg) => ok.push(msg);

function readJSON(path) {
  const abs = join(ROOT, path);
  if (!existsSync(abs)) {
    fail(`Falta el archivo de config: ${path}`);
    return null;
  }
  try {
    const parsed = JSON.parse(readFileSync(abs, "utf8"));
    pass(`JSON válido: ${path}`);
    return parsed;
  } catch (e) {
    fail(`JSON inválido en ${path}: ${e.message}`);
    return null;
  }
}

// --- 1. JSON de config ---------------------------------------------------
const manifest = readJSON(".claude-plugin/plugin.json");
if (manifest) {
  for (const field of ["name", "version", "description"]) {
    if (!manifest[field]) fail(`plugin.json: falta el campo requerido "${field}"`);
  }
}
const mcp = readJSON(".mcp.json");
if (mcp && !mcp.mcpServers) fail(`.mcp.json: falta la clave "mcpServers"`);
const hooks = readJSON("hooks/hooks.json");
const marketplace = readJSON(".claude-plugin/marketplace.json");

// --- 1b. Conformidad con la spec Agent Plugins 1.0.0 ---------------------
// El repo publica el plugin en DOS formatos a la vez:
//   .claude-plugin/plugin.json + .mcp.json  → Claude Code (su formato propio)
//   plugin.json + mcp.json (en la raíz)     → spec agent-plugins.org 1.0.0
// Conviven sin pisarse, pero pueden driftear en silencio: lo de acá abajo es
// lo único que lo impide.
const AP_VERSION = "1.0.0";
const AP_PLUGIN_SCHEMA = `https://agent-plugins.org/schemas/${AP_VERSION}/plugin.schema.json`;
const AP_MCP_SCHEMA = `https://agent-plugins.org/schemas/${AP_VERSION}/mcp.schema.json`;
// El schema de la spec es CERRADO: cualquier otro campo top-level es inválido.
const AP_ALLOWED_FIELDS = new Set([
  "$schema", "name", "version", "description", "author",
  "homepage", "repository", "license", "keywords", "extensions",
]);
const AP_NAME_RE = /^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$/;

const apManifest = readJSON("plugin.json");
if (apManifest) {
  if (apManifest.$schema !== AP_PLUGIN_SCHEMA) {
    fail(`plugin.json (raíz): "$schema" debe ser exactamente "${AP_PLUGIN_SCHEMA}"`);
  }
  if (!apManifest.name) fail(`plugin.json (raíz): falta el campo requerido "name"`);
  else if (!AP_NAME_RE.test(apManifest.name) || apManifest.name.length > 64) {
    fail(`plugin.json (raíz): "name" no cumple el patrón de la spec (minúsculas, sin "--" ni "..", máx 64)`);
  }
  for (const field of Object.keys(apManifest)) {
    if (!AP_ALLOWED_FIELDS.has(field)) {
      fail(`plugin.json (raíz): campo top-level "${field}" no permitido por el schema cerrado de la spec`);
    }
  }
  if (apManifest.author && typeof apManifest.author === "object") {
    for (const k of Object.keys(apManifest.author)) {
      if (!["name", "email", "url"].includes(k)) {
        fail(`plugin.json (raíz): "author.${k}" no está permitido (solo name/email/url)`);
      }
    }
  }
  if (apManifest.extensions) {
    for (const [ns, value] of Object.entries(apManifest.extensions)) {
      if (!ns.includes(".")) fail(`plugin.json (raíz): namespace de extensión "${ns}" no es reverse-domain`);
      if (typeof value !== "object" || value === null || Array.isArray(value)) {
        fail(`plugin.json (raíz): extensions["${ns}"] tiene que ser un objeto`);
      }
    }
  }
  // Los dos manifiestos describen el MISMO plugin: si divergen, un cliente
  // instala una cosa y otro cliente otra.
  if (manifest) {
    for (const field of ["name", "version", "description"]) {
      if (apManifest[field] !== manifest[field]) {
        fail(`Drift entre manifiestos: "${field}" difiere entre plugin.json (raíz) y .claude-plugin/plugin.json`);
      }
    }
    if (!errors.some((e) => e.startsWith("Drift entre manifiestos"))) {
      pass("plugin.json (raíz) y .claude-plugin/plugin.json en sync");
    }
  }
  if (marketplaceVersionMismatch(apManifest.version)) {
    fail(`Drift: marketplace.json metadata.version no coincide con la versión del plugin (${apManifest.version})`);
  }
}

const apMcp = readJSON("mcp.json");
if (apMcp) {
  if (apMcp.$schema !== AP_MCP_SCHEMA) {
    fail(`mcp.json (raíz): "$schema" debe ser exactamente "${AP_MCP_SCHEMA}"`);
  }
  if (!apMcp.mcpServers) fail(`mcp.json (raíz): falta la clave "mcpServers"`);
  else {
    for (const [name, server] of Object.entries(apMcp.mcpServers)) {
      if (!["stdio", "streamable-http", "sse"].includes(server.type)) {
        fail(`mcp.json (raíz): server "${name}" tiene type "${server.type}" — la spec solo define stdio | streamable-http | sse`);
      }
      if (server.type !== "stdio" && !/^https:\/\//.test(server.url ?? "")) {
        fail(`mcp.json (raíz): server "${name}" necesita una URL https absoluta`);
      }
    }
    // Mismo conjunto de servers y mismas URLs que el archivo de Claude Code.
    const claudeServers = Object.keys(mcp?.mcpServers ?? {}).sort().join(",");
    const apServers = Object.keys(apMcp.mcpServers).sort().join(",");
    if (claudeServers !== apServers) {
      fail(`Drift: .mcp.json declara [${claudeServers}] y mcp.json declara [${apServers}]`);
    } else {
      for (const [name, server] of Object.entries(apMcp.mcpServers)) {
        if (server.url !== mcp?.mcpServers?.[name]?.url) {
          fail(`Drift: la URL del server "${name}" difiere entre .mcp.json y mcp.json`);
        }
      }
      pass(".mcp.json y mcp.json apuntan a los mismos servers");
    }
  }
}

/** El marketplace versiona aparte; tiene que seguir al plugin. */
function marketplaceVersionMismatch(version) {
  const mv = marketplace?.metadata?.version;
  return Boolean(version && mv && mv !== version);
}

// Marketplace privado: parsea, tiene plugins, y cada source apunta a un plugin real.
if (marketplace) {
  if (!marketplace.name) fail(`marketplace.json: falta el campo "name"`);
  if (!Array.isArray(marketplace.plugins) || !marketplace.plugins.length) {
    fail(`marketplace.json: "plugins" tiene que ser un array con al menos un plugin`);
  } else {
    for (const p of marketplace.plugins) {
      if (!p.name) fail(`marketplace.json: un plugin no tiene "name"`);
      const src = p.source ?? "./";
      const pluginJson = join(ROOT, src, ".claude-plugin", "plugin.json");
      if (existsSync(pluginJson)) pass(`marketplace.json → plugin "${p.name}" (source ${src}) existe`);
      else fail(`marketplace.json → plugin "${p.name}": no hay plugin.json en ${src}`);
    }
  }
}

// --- 2 + 3. Skills: frontmatter + referencias ----------------------------
const skillsDir = join(ROOT, "skills");
// core/skills = el canon compartido (F4): mismas reglas de validación.
const coreSkillsDir = join(ROOT, "core", "skills");
const coreSkills = existsSync(coreSkillsDir)
  ? readdirSync(coreSkillsDir)
      .filter((d) => statSync(join(coreSkillsDir, d)).isDirectory())
      .map((d) => ({ name: d, dir: join(coreSkillsDir, d), label: `core/skills/${d}` }))
  : [];
for (const core of coreSkills) {
  const md = join(core.dir, "SKILL.md");
  if (!existsSync(md)) {
    fail(`${core.label}: falta SKILL.md`);
    continue;
  }
  const content = readFileSync(md, "utf8");
  const fm = content.match(/^---\n([\s\S]*?)\n---/);
  if (!fm) {
    fail(`${core.label}/SKILL.md: falta el frontmatter (---)`);
  } else {
    const nameMatch = fm[1].match(/^name:\s*(\S.*)$/m);
    if (nameMatch && nameMatch[1].trim().replace(/^"|"$/g, "") !== core.name) {
      fail(`${core.label}/SKILL.md: frontmatter name no coincide con la carpeta`);
    } else {
      pass(`${core.label}: canon OK`);
    }
  }
}

const skills = existsSync(skillsDir)
  ? readdirSync(skillsDir).filter((d) => statSync(join(skillsDir, d)).isDirectory())
  : [];

if (!skills.length) fail("No se encontró ninguna skill en skills/");

for (const skill of skills) {
  const skillDir = join(skillsDir, skill);
  const skillMd = join(skillDir, "SKILL.md");
  if (!existsSync(skillMd)) {
    fail(`skills/${skill}: falta SKILL.md`);
    continue;
  }
  const content = readFileSync(skillMd, "utf8");

  // Frontmatter YAML mínimo + name debe coincidir con la carpeta (evita el
  // caso "Cinematografic Video" de la 0.3: nombre roto que no matchea nada).
  const fm = content.match(/^---\n([\s\S]*?)\n---/);
  if (!fm) {
    fail(`skills/${skill}/SKILL.md: falta el frontmatter (---)`);
  } else {
    if (!/^name:\s*\S/m.test(fm[1])) fail(`skills/${skill}/SKILL.md: frontmatter sin "name"`);
    if (!/^description:\s*\S/m.test(fm[1])) fail(`skills/${skill}/SKILL.md: frontmatter sin "description"`);
    const nameMatch = fm[1].match(/^name:\s*(\S.*)$/m);
    if (nameMatch && nameMatch[1].trim() !== skill) {
      fail(`skills/${skill}/SKILL.md: frontmatter name "${nameMatch[1].trim()}" no coincide con la carpeta "${skill}"`);
    }
  }

  // `skill.md` en minúscula rompe en Linux/CI (el archivo real es SKILL.md).
  if (/`skill\.md`|\bskill\.md\b/.test(content.replaceAll("SKILL.md", ""))) {
    fail(`skills/${skill}/SKILL.md: menciona "skill.md" en minúscula (es SKILL.md, case-sensitive)`);
  }

  // Referencias a archivos/carpetas INTERNAS de la skill: tokens entre backticks
  // que parezcan rutas relativas (contienen "/" y terminan en .md o en "/") y cuyo
  // primer segmento sea una carpeta estándar de skill. Las rutas de salida en la
  // carpeta del cliente (brand/, productos/, entregables/…) son runtime, no archivos
  // del repo — no se chequean.
  const SKILL_DIRS = new Set(["instructions", "style", "templates", "examples", "eval"]);
  const refs = new Set();
  for (const m of content.matchAll(/`([\w./-]+)`/g)) {
    const token = m[1];
    if (!token.includes("/")) continue;
    if (!(token.endsWith(".md") || token.endsWith("/"))) continue;
    if (!SKILL_DIRS.has(token.split("/")[0])) continue;
    refs.add(token);
  }

  let brokenInSkill = 0;
  for (const ref of refs) {
    const target = join(skillDir, ref);
    if (!existsSync(target)) {
      fail(`skills/${skill}/SKILL.md → referencia rota: \`${ref}\` (no existe ${rel(target)})`);
      brokenInSkill++;
    } else if (!caseExactExists(target)) {
      // macOS es case-insensitive: existsSync pasa pero Linux/CI rompe.
      fail(`skills/${skill}/SKILL.md → referencia con case incorrecto: \`${ref}\``);
      brokenInSkill++;
    }
  }
  if (!brokenInSkill) pass(`skills/${skill}: ${refs.size} referencias verificadas, frontmatter OK`);
}

/** existsSync con case EXACTO (macOS es case-insensitive; Linux no). */
function caseExactExists(target) {
  const parts = rel(target).split("/").filter(Boolean);
  let current = ROOT;
  for (const part of parts) {
    let entries;
    try {
      entries = readdirSync(current);
    } catch {
      return false;
    }
    if (!entries.includes(part)) return false;
    current = join(current, part);
  }
  return true;
}

// --- 4. Hook de SessionStart apunta a un archivo real --------------------
if (hooks?.SessionStart) {
  for (const entry of hooks.SessionStart) {
    for (const h of entry.hooks ?? []) {
      const m = (h.command ?? "").match(/CLAUDE_PLUGIN_ROOT\}\/([\w./-]+)/);
      if (m) {
        const target = join(ROOT, m[1]);
        if (existsSync(target)) pass(`hook SessionStart → ${m[1]} existe`);
        else fail(`hook SessionStart → archivo inexistente: ${m[1]}`);
      }
    }
  }
}

// --- Reporte -------------------------------------------------------------
for (const line of ok) console.log(`  ✓ ${line}`);
if (errors.length) {
  console.error(`\n✗ ${errors.length} problema(s):\n`);
  for (const e of errors) console.error(`  ✗ ${e}`);
  process.exit(1);
}
console.log(`\n✓ Plugin válido — ${ok.length} chequeos pasados.`);
