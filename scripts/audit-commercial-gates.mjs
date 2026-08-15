#!/usr/bin/env node
/**
 * KTS commercial gates audit（2026-08-16 扩展：consent 修复任务）
 *
 * 契约：
 *  - AdSense：publisher 数据保持 raw pub- 形式；三个 serving 闸门默认全 false；
 *    默认输出零 adsbygoogle 脚本；fixture 强制开启时每页恰好一个脚本且无 raw pub 泄漏；
 *    ownership meta / ads.txt 不变。
 *  - GamersGate：联盟配置不变；计佣链接带 ?aff=ID + rel="sponsored nofollow noopener"；
 *    普通 Steam/来源链接不带 sponsored；affiliate_click / outbound_click 事件语义保留。
 *  - 预同意零可选 provider 静态脚本；同意控件（accept/reject/settings/save/withdraw）齐全。
 *  - 两次默认构建字节一致（确定性）。
 *  - fault 子进程（KTS_COMMERCIAL_AUDIT_FAULT）：adsense-serving / affiliate-contamination
 *    必须因预期原因非零退出。
 */
import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const script = fileURLToPath(import.meta.url);
const publicDir = path.join(root, "public");
const sitePath = path.join(root, "data", "site.json");
const basePath = path.join(root, "data", "site.base.json");
const generatorPath = path.join(root, "scripts", "generate.js");
const fault = process.env.KTS_COMMERCIAL_AUDIT_FAULT || "";
const expectedPublisher = "pub-4174270222899193";
const expectedClient = `ca-${expectedPublisher}`;
const expectedGamersGateId = "01352e74c147aa8c9ae9c2793e51726c1e005035";
const ADSENSE_SERVING_URL = "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js";
const OPTIONAL_PROVIDER_TAG = /<script[^>]+src=["'][^"']*(?:googletagmanager\.com|effectivecpmnetwork\.com)[^"']*["'][^>]*>/i;

const readJson = file => JSON.parse(fs.readFileSync(file, "utf8"));
const count = (text, needle) => text.split(needle).length - 1;
const filesUnder = dir => fs.readdirSync(dir, { withFileTypes: true })
  .flatMap(entry => entry.isDirectory()
    ? filesUnder(path.join(dir, entry.name))
    : [path.join(dir, entry.name)])
  .sort();
const htmlFiles = () => filesUnder(publicDir).filter(file => file.endsWith(".html"));
const htmlCorpus = () => htmlFiles().map(file => fs.readFileSync(file, "utf8")).join("\n");
const treeHash = () => {
  const hash = crypto.createHash("sha256");
  for (const file of filesUnder(publicDir)) {
    hash.update(path.relative(publicDir, file));
    hash.update("\0");
    hash.update(fs.readFileSync(file));
    hash.update("\0");
  }
  return hash.digest("hex");
};
const runBuild = fixture => {
  const env = { ...process.env };
  delete env.KTS_ADSENSE_FIXTURE;
  if (fixture) {
    env.NODE_ENV = "test";
    env.KTS_ADSENSE_FIXTURE = "enabled";
  }
  const result = spawnSync(process.execPath, [generatorPath], {
    cwd: root,
    env,
    encoding: "utf8",
  });
  assert.equal(result.status, 0, result.stderr || result.stdout || "generator failed");
  return result.stdout.trim();
};
const sitemapFiles = () => {
  const xml = fs.readFileSync(path.join(publicDir, "sitemap.xml"), "utf8");
  const urls = [...xml.matchAll(/<loc>https:\/\/[^/]+(\/[^<]*)<\/loc>/g)].map(match => match[1]);
  return urls.map(route => {
    const relative = route.endsWith("/")
      ? `${route.replace(/^\//, "")}index.html`
      : `${route.replace(/^\//, "")}.html`;
    return path.join(publicDir, relative);
  });
};

/* ---------- 数据 + 生成器源码闸门（fault 子进程同样执行） ---------- */
const base = readJson(basePath);
const site = readJson(sitePath);
for (const data of [base, site]) {
  assert.equal(data.site.adsenseId, expectedPublisher, "AdSense publisher data must stay in raw pub- form");
  assert.deepEqual(data.site.adsenseServing, {
    enabled: false,
    providerReady: false,
    certifiedCmpReady: false,
  }, "all three production serving gates must default false");
  assert.deepEqual(data.site.affiliates?.["gamersgate.com"], {
    type: "param",
    param: "aff",
    value: expectedGamersGateId,
  }, "verified GamersGate affiliate configuration changed");
}

const generatorSource = fs.readFileSync(generatorPath, "utf8");
assert.equal(generatorSource.includes("cozysimhub20-20"), false, "retired Amazon tag remains in generator");
assert.equal(generatorSource.includes("renderAmazonAffiliate"), false, "retired Amazon renderer remains in generator");

/* ---------- corpus 级商业 + 同意在场检查（供 fault 子进程复用） ---------- */
function assertCommercialCorpus(corpus) {
  assert.equal(corpus.includes("amazon-gear"), false, "default output still contains an Amazon module");
  assert.equal(corpus.includes("cozysimhub20-20"), false, "default output still contains the retired Amazon tag");
  assert.equal(/https:\/\/(?:www\.)?amazon\.[^\s"'<]+/i.test(corpus), false, "default output still contains an Amazon URL");
  assert.equal(corpus.includes(ADSENSE_SERVING_URL), false,
    "default output must not load the AdSense serving script");
  assert.equal(fs.readFileSync(path.join(publicDir, "ads.txt"), "utf8"),
    `google.com, ${expectedPublisher}, DIRECT, f08c47fec0942fa0\n`, "ads.txt raw publisher record changed");
  assert.equal(corpus.includes(`aff=${expectedGamersGateId}`), true, "verified GamersGate tracking URL disappeared");
  assert.equal(/gamersgate\.com[^>]+rel="[^"]*\bsponsored\b[^"]*"/i.test(corpus), true,
    "GamersGate sponsored relationship disappeared");
  assert.equal(corpus.includes("affiliate_click"), true, "affiliate_click intent event disappeared");
  assert.equal(corpus.includes("outbound_click"), true, "outbound_click intent event disappeared");
  assert.equal(/<a[^>]*store\.steampowered\.com[^>]*rel="[^"]*\bsponsored\b[^"]*"/i.test(corpus), false,
    "ordinary Steam link became sponsored");
  assert.equal(OPTIONAL_PROVIDER_TAG.test(corpus), false,
    "optional provider script loaded before consent");
  for (const token of ["data-consent-settings", "data-consent-accept", "data-consent-reject",
    "data-consent-save", "data-consent-withdraw"])
    assert.equal(corpus.includes(token), true, `consent control ${token} missing`);
}

/* ---------- fault 子进程：按预期原因非零退出 ---------- */
if (fault === "adsense-serving") {
  // 模拟「投放被开启」：fixture 构建会产生 adsbygoogle 脚本，
  // 默认闸门检查（零 serving）必须能抓住它。
  runBuild(true);
  let caught = false;
  try { assertCommercialCorpus(htmlCorpus()); } catch (_) { caught = true; }
  runBuild(false); // 还原默认输出
  if (!caught) { console.error("fault adsense-serving: enablement was not caught by the audit"); process.exit(0); }
  console.error("fault adsense-serving: detected — serving enablement fails the default gate");
  process.exit(1);
}
if (fault === "affiliate-contamination") {
  // 模拟「GamersGate 链接被去 sponsored」（5 语 where-to-buy 全部去赞助标记）：
  // 审计的计佣关系检查必须能抓住它。
  runBuild(false);
  const corpus = htmlFiles().map(file => {
    let html = fs.readFileSync(file, "utf8");
    if (/where-to-buy\.html$/.test(file)) html = html.replace('rel="sponsored nofollow noopener"', 'rel="noopener"');
    return html;
  }).join("\n");
  let caught = false;
  try { assertCommercialCorpus(corpus); } catch (_) { caught = true; }
  if (!caught) { console.error("fault affiliate-contamination: de-sponsored links were not caught by the audit"); process.exit(0); }
  console.error("fault affiliate-contamination: detected — de-sponsored GamersGate links fail the audit");
  process.exit(1);
}
if (fault) {
  console.error(`unknown commercial audit fault: ${fault}`);
  process.exit(1);
}

/* ---------- 主流程 ---------- */
const firstDefaultBuild = runBuild(false);
const firstDefaultHash = treeHash();
assertCommercialCorpus(htmlCorpus());
const indexableFiles = sitemapFiles();
assert.equal(indexableFiles.length, site.site.languages.length * (site.pages.length + 4), "five-language route set is incomplete");
for (const file of indexableFiles) {
  assert.equal(fs.existsSync(file), true, `missing indexable output ${path.relative(publicDir, file)}`);
  const html = fs.readFileSync(file, "utf8");
  assert.equal(count(html, `<meta name="google-adsense-account" content="${expectedClient}" />`), 1,
    `AdSense ownership meta count mismatch in ${path.relative(publicDir, file)}`);
}
// 每页计佣链接数量：只有 where-to-buy（5 语）各带 1 条 sponsored 链接
for (const file of htmlFiles()) {
  const html = fs.readFileSync(file, "utf8");
  const isBuy = /where-to-buy\.html$/.test(file);
  assert.equal(count(html, 'rel="sponsored nofollow noopener"'), isBuy ? 1 : 0,
    `sponsored link count mismatch in ${path.relative(publicDir, file)}`);
}

const secondDefaultBuild = runBuild(false);
const secondDefaultHash = treeHash();
assert.equal(secondDefaultHash, firstDefaultHash, "two default builds are not byte-identical");

const fixtureBuild = runBuild(true);
for (const file of htmlFiles()) {
  const html = fs.readFileSync(file, "utf8");
  assert.equal(count(html, ADSENSE_SERVING_URL), 1,
    `enabled fixture must emit exactly one AdSense script in ${path.relative(publicDir, file)}`);
  assert.equal(count(html, `client=${expectedClient}`), 1,
    `enabled fixture client mismatch in ${path.relative(publicDir, file)}`);
  assert.equal(html.includes("client=pub-"), false, `raw pub client leaked in ${path.relative(publicDir, file)}`);
  assert.equal(html.includes("client=ca-ca-pub-"), false, `double ca- prefix in ${path.relative(publicDir, file)}`);
}

runBuild(false);
assert.equal(treeHash(), firstDefaultHash, "fixture round-trip did not restore byte-identical default output");

const negative = {};
for (const name of ["adsense-serving", "affiliate-contamination"]) {
  const result = spawnSync(process.execPath, [script, root], {
    env: { ...process.env, KTS_COMMERCIAL_AUDIT_FAULT: name },
    encoding: "utf8",
  });
  negative[name] = result.status;
  assert.notEqual(result.status, 0, `negative fixture ${name} did not fail for its intended reason`);
}

console.log(JSON.stringify({
  status: "pass",
  locales: site.site.languages.length,
  pages: htmlFiles().length,
  indexablePages: indexableFiles.length,
  defaultServingScripts: 0,
  fixtureScriptsPerPage: 1,
  publisherId: expectedPublisher,
  clientId: expectedClient,
  sponsoredLinkPages: 5,
  defaultTreeSha256: firstDefaultHash,
  negativeFaultExitCodes: negative,
  builds: [firstDefaultBuild, secondDefaultBuild, fixtureBuild],
}, null, 2));
