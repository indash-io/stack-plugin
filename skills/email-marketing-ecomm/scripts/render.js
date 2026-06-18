#!/usr/bin/env node
/**
 * Renderiza todos los .html de una carpeta a .png full-page.
 *
 * Uso:
 *   node scripts/render.js <folder>
 *
 * Ejemplo:
 *   node scripts/render.js output/2026-04-23_3x2-ice-roller
 *
 * Renderiza cada HTML a un PNG del mismo nombre, ancho 600px (email real),
 * full-page (scroll completo capturado).
 */

const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

async function main() {
  const folder = process.argv[2];
  if (!folder) {
    console.error('Usage: node scripts/render.js <folder>');
    process.exit(1);
  }

  const absFolder = path.resolve(folder);
  if (!fs.existsSync(absFolder)) {
    console.error(`Folder not found: ${absFolder}`);
    process.exit(1);
  }

  const htmlFiles = fs.readdirSync(absFolder).filter((f) => f.endsWith('.html'));
  if (htmlFiles.length === 0) {
    console.error(`No HTML files found in ${absFolder}`);
    process.exit(1);
  }

  console.log(`Found ${htmlFiles.length} HTML files. Launching browser...`);
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  for (const file of htmlFiles) {
    const htmlPath = path.join(absFolder, file);
    const pngPath = path.join(absFolder, file.replace(/\.html$/, '.png'));

    const page = await browser.newPage();
    await page.setViewport({ width: 600, height: 800, deviceScaleFactor: 2 });
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });

    // Esperar que las imágenes externas carguen
    await page.evaluate(() =>
      Promise.all(
        Array.from(document.images)
          .filter((img) => !img.complete)
          .map(
            (img) =>
              new Promise((resolve) => {
                img.onload = img.onerror = resolve;
              })
          )
      )
    );

    await page.screenshot({
      path: pngPath,
      fullPage: true,
      type: 'png',
    });
    console.log(`  ✓ ${file} → ${path.basename(pngPath)}`);
    await page.close();
  }

  await browser.close();
  console.log('Done.');
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
