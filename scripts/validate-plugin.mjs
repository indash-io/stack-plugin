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

// Marketplace privado: parsea, tiene plugins, y cada source apunta a un plugin real.
const marketplace = readJSON(".claude-plugin/marketplace.json");
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

  // Frontmatter YAML mínimo
  const fm = content.match(/^---\n([\s\S]*?)\n---/);
  if (!fm) {
    fail(`skills/${skill}/SKILL.md: falta el frontmatter (---)`);
  } else {
    if (!/^name:\s*\S/m.test(fm[1])) fail(`skills/${skill}/SKILL.md: frontmatter sin "name"`);
    if (!/^description:\s*\S/m.test(fm[1])) fail(`skills/${skill}/SKILL.md: frontmatter sin "description"`);
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
    }
  }
  if (!brokenInSkill) pass(`skills/${skill}: ${refs.size} referencias verificadas, frontmatter OK`);
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
