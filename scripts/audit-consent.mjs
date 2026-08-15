#!/usr/bin/env node
/**
 * KTS consent/privacy audit（2026-08-16，consent 修复任务）
 *
 * 契约：
 *  1) 101 页静态 HTML 零可选 provider 脚本标签（GA4/Adsterra/AdSense 全部不得预载）；
 *  2) 每页都有完整的五语同意控件：accept/reject/settings(manage)/save/withdraw/dialog +
 *     analytics/advertising 复选框；<dialog> 模态焦点圈闭、Escape 关闭并归还焦点；
 *  3) reject/withdraw 必须持久化全 false（默认/拒绝/撤回后零请求），
 *     accept/save 才加载，且每页每 provider 至多一次（duplicate-load guard）；
 *  4) Adsterra provider src + container id 每页只出现在 consent cfg JSON 中（各 1 次），
 *     footer 区域不得出现 provider 脚本；
 *  5) 五份隐私页准确披露 GA4/Adsterra/effectivecpmnetwork、本地偏好存储 kts_consent_v1、
 *     Cookie/标识符、默认关闭、撤回、非 Google 认证 CMP；无匿名/无 PII 绝对化表述；
 *  6) 独立 fault 注入：每个 fault 子进程（KTS_CONSENT_AUDIT_FAULT）必须因预期原因非零退出。
 */
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const script = fileURLToPath(import.meta.url);
const root = path.resolve(process.argv[2] || path.join(path.dirname(script), ".."));
const pub = path.join(root, "public");
const fault = process.env.KTS_CONSENT_AUDIT_FAULT || "";
const failures = [];
const fail = (code, detail) => failures.push({ code, detail });
const count = (text, needle) => needle ? text.split(needle).length - 1 : 0;
const walk = (dir, out = []) => {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, entry.name);
    entry.isDirectory() ? walk(file, out) : entry.name.endsWith(".html") && out.push(file);
  }
  return out;
};

const providerHost = "pl30754215.effectivecpmnetwork.com";
const providerContainer = "container-0c46b4f927b15d9a891d95122869e902";
const gaHost = "www.googletagmanager.com/gtag/js";

/** fault 注入：只改一个文件，模拟对应的回归；其余页面保持真实输出 */
function inject(relative, html) {
  if (fault === "no-choice-network" && relative === "index.html") {
    return html.replace("</head>", `<script src="https://${gaHost}?id=G-FAULT"></script></head>`);
  }
  if (fault === "reject-network" && relative === "index.html") {
    return html.replace(
      "document.querySelector('[data-consent-reject]').addEventListener('click',function(){persist({analytics:false,advertising:false});});",
      "document.querySelector('[data-consent-reject]').addEventListener('click',function(){persist({analytics:true,advertising:true});});",
    );
  }
  if (fault === "withdraw-loss" && relative === "index.html") {
    return html.replace(
      "document.querySelector('[data-consent-withdraw]').addEventListener('click',function(){persist({analytics:false,advertising:false});});",
      "document.querySelector('[data-consent-withdraw]').addEventListener('click',function(){persist({analytics:true,advertising:true});});",
    );
  }
  if (fault === "duplicate-provider" && relative === "index.html") {
    return html
      .replace("gaLoaded||document.getElementById('kts-ga4-script')", "false")
      .replace("adLoaded||document.getElementById('kts-adsterra-script')", "false");
  }
  if (fault === "focus-escape" && relative === "index.html") {
    return html
      .replace("<dialog id=\"consent-dialog-", "<section id=\"consent-dialog-")
      .replace("</dialog>", "</section>")
      .replace("if(!dialog.open)dialog.showModal();", "dialog.hidden=false;");
  }
  if (fault === "privacy-missing" && relative === "privacy.html") {
    return html.replace("first-party preference control", "first-party preference panel");
  }
  if (fault === "privacy-fallback" && relative === "zh-CN/privacy.html") {
    return html.replace("本站自有的偏好控制", "first-party preference control");
  }
  return html;
}

if (!fs.existsSync(pub)) fail("missing-public", pub);
const rows = failures.length ? [] : walk(pub).map(file => {
  const relative = path.relative(pub, file).split(path.sep).join("/");
  return { relative, html: inject(relative, fs.readFileSync(file, "utf8")) };
});

if (rows.length && rows.length !== 101) fail("html-count", rows.length);
for (const { relative, html } of rows) {
  const initialOptional = [...html.matchAll(/<script[^>]+src=["']([^"']*(?:googletagmanager|effectivecpmnetwork)[^"']*)["']/gi)];
  if (initialOptional.length) fail("no-choice-network", `${relative}:${initialOptional.map(x => x[1]).join(",")}`);
  if (html.includes("pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"))
    fail("adsense-serving-in-default", relative);
  for (const token of ["data-consent-accept", "data-consent-reject", "data-consent-settings", "data-consent-save", "data-consent-withdraw", "data-consent-dialog", "data-consent-analytics", "data-consent-advertising"]) {
    if (count(html, token) < 1) fail("control-missing", `${relative}:${token}`);
  }
  if (!html.includes("aria-controls=\"consent-dialog-") || !html.includes("aria-expanded=\"false\""))
    fail("settings-a11y", relative);
  if (!html.includes("<dialog id=\"consent-dialog-") ||
      !html.includes("if(!dialog.open)dialog.showModal();") ||
      !html.includes("dialog.addEventListener('cancel',function(e){e.preventDefault();close();});") ||
      !html.includes("dialog.addEventListener('keydown',function(e){if(e.key!=='Tab')return;"))
    fail("focus-boundary", relative);
  if (!html.includes("document.querySelector('[data-consent-reject]').addEventListener('click',function(){persist({analytics:false,advertising:false});});"))
    fail("reject-not-blocking", relative);
  if (!html.includes("document.querySelector('[data-consent-withdraw]').addEventListener('click',function(){persist({analytics:false,advertising:false});});"))
    fail("withdraw-not-blocking", relative);
  if (!html.includes("document.querySelector('[data-consent-accept]').addEventListener('click',function(){persist({analytics:true,advertising:true});});"))
    fail("accept-not-loading", relative);
  if (!html.includes("gaLoaded||document.getElementById('kts-ga4-script')") ||
      !html.includes("adLoaded||document.getElementById('kts-adsterra-script')"))
    fail("duplicate-load-guard", relative);
  if (!html.includes("banner.hidden||!banner.contains(document.activeElement)"))
    fail("banner-escape-ownership", relative);
  const footer = (html.match(/<footer class="site-footer">[\s\S]*?<\/footer>/) || [""])[0];
  if (footer.includes(providerHost) || footer.includes(providerContainer)) fail("footer-provider-leak", relative);
  if (!html.includes("data-adsterra-mount")) fail("adsterra-mount-missing", relative);
  // provider 配置只允许出现在 consent cfg JSON（各 1 次）
  if (count(html, providerHost) !== 1) fail("provider-config-count", `${relative}:${count(html, providerHost)}`);
  if (count(html, providerContainer) !== 1) fail("provider-container-count", `${relative}:${count(html, providerContainer)}`);
  if (!html.includes("kts_consent_v1")) fail("local-preference-key", relative);
}

const privacyMarkers = {
  "privacy.html": { boundary: "first-party preference control", cookie: "cookies or similar identifiers" },
  "zh-CN/privacy.html": { boundary: "本站自有的偏好控制", cookie: "Cookie 或类似标识符" },
  "zh-TW/privacy.html": { boundary: "本站自有的偏好控制", cookie: "Cookie 或類似識別碼" },
  "ja/privacy.html": { boundary: "本サイト独自の設定機能", cookie: "Cookie や類似の識別子" },
  "ko/privacy.html": { boundary: "사이트 자체 선택 설정", cookie: "쿠키나 유사 식별자" },
};
const policyUrls = [
  "https://policies.google.com/privacy",
  "https://adsterra.com/privacy-policy/",
];
for (const [relative, markers] of Object.entries(privacyMarkers)) {
  const html = rows.find(row => row.relative === relative)?.html || "";
  if (!html) { fail("privacy-locale-missing", relative); continue; }
  for (const token of ["Google Analytics", "GA4", "Adsterra", "effectivecpmnetwork", "kts_consent_v1", markers.cookie, markers.boundary]) {
    if (!html.includes(token)) fail("privacy-disclosure", `${relative}:${token}`);
  }
  for (const url of policyUrls) if (!html.includes(url)) fail("privacy-policy-link", `${relative}:${url}`);
  const visible = html.replace(/<script[\s\S]*?<\/script>/gi, " ").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ");
  if (/anonymous data|no personally identifiable|匿名数据|匿名資料|匿名データ|익명 데이터/i.test(visible))
    fail("absolute-privacy-claim", relative);
}

const negative = {};
if (!fault && !failures.length) {
  for (const name of ["no-choice-network", "reject-network", "withdraw-loss", "duplicate-provider", "focus-escape", "privacy-missing", "privacy-fallback"]) {
    const result = spawnSync(process.execPath, [script, root], {
      env: { ...process.env, KTS_CONSENT_AUDIT_FAULT: name },
      encoding: "utf8",
    });
    negative[name] = result.status;
    if (result.status === 0) fail("negative-fixture-did-not-fail", name);
  }
}

console.log(JSON.stringify({
  status: failures.length ? "fail" : "pass",
  html_pages: rows.length,
  privacy_locales: Object.keys(privacyMarkers).length,
  negative_fixture_exit_codes: negative,
  failures,
}, null, 2));
process.exit(failures.length ? 1 : 0);
