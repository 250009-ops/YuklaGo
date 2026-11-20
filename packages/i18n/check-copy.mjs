#!/usr/bin/env node
/**
 * Fails if a banned phrase appears in product copy.
 * Scans apps/, packages/ui/, and packages/i18n/locales/ when those files exist.
 * Does not scan docs/. The handbook has to name the banned phrases.
 *
 *   node packages/i18n/check-copy.mjs
 *   node packages/i18n/check-copy.mjs --self-test
 */

import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "../..");
const banned = JSON.parse(
  readFileSync(join(root, "packages/i18n/banned-phrases.json"), "utf8"),
);
const mustShow = JSON.parse(
  readFileSync(join(root, "packages/i18n/must-show.json"), "utf8"),
);

function fold(value) {
  return value
    .normalize("NFC")
    .replace(/[\u2018\u2019\u02BB\u02BC`']/g, "'")
    .toLowerCase();
}

const forms = banned.phrases.flatMap((phrase) =>
  phrase.forms.map((form) => ({ id: phrase.id, form: fold(form) })),
);

function walk(dir, out) {
  if (!existsSync(dir)) return;
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    const stat = statSync(path);
    if (stat.isDirectory()) {
      if (name === "node_modules" || name === "fixtures") continue;
      walk(path, out);
    } else if (/\.(json|tsx|ts|jsx|js|html|vue)$/.test(name)) {
      out.push(path);
    }
  }
}

function scanFile(path) {
  const text = fold(readFileSync(path, "utf8"));
  const hits = [];
  for (const item of forms) {
    if (text.includes(item.form)) hits.push(item.id);
  }
  return hits;
}

function checkLocales() {
  const missing = [];
  for (const lang of ["uz", "ru"]) {
    const file = join(root, "packages/i18n/locales", `${lang}.json`);
    const text = readFileSync(file, "utf8");
    for (const line of mustShow.lines) {
      if (!text.includes(line[lang])) missing.push(`${lang}:${line.id}`);
    }
  }
  return missing;
}

function collectProductFiles() {
  const files = [];
  walk(join(root, "apps"), files);
  walk(join(root, "packages/ui"), files);
  walk(join(root, "packages/i18n/locales"), files);
  return files;
}

if (process.argv.includes("--self-test")) {
  const bad = scanFile(join(root, "packages/i18n/fixtures/bad-uz.txt"));
  if (!bad.includes("broker-replaces")) {
    console.error("self-test: fixture was not detected");
    process.exit(1);
  }
  const localeHits = collectProductFiles().flatMap((file) =>
    scanFile(file).map((id) => `${file} ${id}`),
  );
  if (localeHits.length) {
    console.error(localeHits.join("\n"));
    process.exit(1);
  }
  const missing = checkLocales();
  if (missing.length) {
    console.error("self-test missing must-show lines: " + missing.join(", "));
    process.exit(1);
  }
  console.log("copy self-test ok");
  process.exit(0);
}

const hits = [];
for (const file of collectProductFiles()) {
  for (const id of scanFile(file)) hits.push(`${file}: ${id}`);
}
const missing = checkLocales();
if (missing.length) {
  console.error("Missing must-show lines:\n" + missing.join("\n"));
}
if (hits.length) {
  console.error("Banned phrases:\n" + hits.join("\n"));
}
if (hits.length || missing.length) process.exit(1);
console.log("copy check ok");
