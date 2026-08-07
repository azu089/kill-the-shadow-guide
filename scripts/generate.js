#!/usr/bin/env node
/**
 * KTS Guide Static Site Generator — "Case File Noir" theme (v2)
 * 数据驱动 + 5 语言：data/site.json → node scripts/generate.js → public/
 * 语言：en（默认，根路径）/ zh-CN / zh-TW / ja / ko，hreflang + 语言切换器
 * 视觉：案件卷宗 noir（碳黑+血红+琥珀、证据标签、案件板 hero、侦探工具图标）
 */
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const ROOT = path.join(__dirname, "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "site.json"), "utf8"));
const OUT = path.join(ROOT, "public");
const KIT = require("./lib/site-kit");   // 共用基建：URL/图片/sitemap/lastmod
// 联盟链接：site.json 的 affiliates 没配 ID 时原样输出原链接，配了才加追踪参数 + rel="sponsored"
const AFF = KIT.createAffiliate(DATA.site.affiliates);
const esc = KIT.esc;
const clean = KIT.clean;
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8")).digest("hex").slice(0,8);
const today = new Date().toISOString().slice(0,10);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
const LM = KIT.createLastmod({ manifestPath: path.join(ROOT,"data",".lastmod.json"), today });
const HERO_SET = "/images/hero-640.jpg 640w, /images/hero-1280.jpg 1280w, /images/hero.jpg 1600w";
const LANG_META = {
  "en":    { flag: "🇬🇧", name: "English",  html: "en" },
  "zh-CN": { flag: "🇨🇳", name: "简体中文", html: "zh-CN" },
  "zh-TW": { flag: "🇹🇼", name: "繁體中文", html: "zh-TW" },
  "ja":    { flag: "🇯🇵", name: "日本語",   html: "ja" },
  "ko":    { flag: "🇰🇷", name: "한국어",   html: "ko" },
};
/* ---------- SVG flags (premium, render on all platforms) ---------- */
const FLAGS = {
  "en": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#012169"/><path d="M0 0 60 40M60 0 0 40" stroke="#fff" stroke-width="11"/><path d="M0 0 60 40M60 0 0 40" stroke="#C8102E" stroke-width="6"/><path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="14"/><path d="M30 0v40M0 20h60" stroke="#C8102E" stroke-width="8"/></svg>',
  "zh-CN": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#EE1C25"/><g fill="#FFDE00"><path d="M12 8l1.7 3.4 3.8.5-2.8 2.7.7 3.8L12 16.7l-3.4 1.7.7-3.8-2.8-2.7 3.8-.5z"/><path d="M22 4l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM25 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM22 18l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM19 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3z"/></g></svg>',
  "zh-TW": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#FE0000"/><rect width="30" height="20" fill="#000095"/><g fill="#fff" stroke="#fff" stroke-width="1"><path d="M15 2l2.3 6.7 7 .1-5.6 4.2 2.1 6.7-5.8-4-5.8 4 2.1-6.7L5.7 8.8l7-.1z"/><g stroke-width=".6"><path d="M15 2v16M15 2 5.7 8.8 15 15.6M15 2l9.3 6.8L15 15.6M15 2v16M15 18.8 5.7 12 15 5.2M15 18.8l9.3-6.8L15 5.2"/></g></g></svg>',
  "ja": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#BC002D"/></svg>',
  "ko": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><g transform="translate(30 20)"><g transform="rotate(45)"><rect x="-10" y="-5" width="20" height="10" fill="#CD2E3A"/><rect x="-10" y="0" width="20" height="10" fill="#0047A0"/><circle r="6" fill="#fff"/></g><circle r="5" fill="#CD2E3A"/><path d="M0-5a5 5 0 0 1 0 10 2 2 0 0 1 0-10" fill="#0047A0"/></g><g fill="#000"><path d="M15 2h3v6h-3zM15 32h3v6h-3zM42 2h3v6h-3zM42 32h3v6h-3z"/></g></svg>',
};
const flagOf = lang => FLAGS[lang] || "🌐";

const metaOf = slug => (DATA.pages.find(p=>p.slug===slug)?.meta) || {};
const pageOf = (page, lang) => {
  if (lang === DEF || !page.i18n || !page.i18n[lang]) {
    return { title: page.title, metaTitle: page.metaTitle, metaDescription: page.metaDescription, intro: page.intro, sections: page.sections, heroImage: page.heroImage };
  }
  const t = page.i18n[lang];
  return { title: t.title || page.title, metaTitle: t.metaTitle || page.metaTitle, metaDescription: t.metaDescription || page.metaDescription, intro: t.intro || page.intro, sections: t.sections || page.sections, heroImage: t.heroImage || page.heroImage };
};
const siteI18n = lang => {
  const s = (DATA.site.i18n && DATA.site.i18n[lang]) || {};
  return {
    name: s.name || DATA.site.name, tagline: s.tagline || DATA.site.tagline, description: s.description || DATA.site.description,
    navHome: s.navHome || "Home", navGuides: s.navGuides || "Guides", navCases: s.navCases || "Case Board", navCharacters: s.navCharacters || "Characters",
    navAbout: s.navAbout || "About", navPrivacy: s.navPrivacy || "Privacy", navContact: s.navContact || "Contact",
    langLabel: s.langLabel || "Language", aboutTitle: s.aboutTitle || "About", privacyTitle: s.privacyTitle || "Privacy Policy", contactTitle: s.contactTitle || "Contact",
    footerNote: s.footerNote || "Unofficial fan site — game and related assets belong to their respective owners.",
    footerSource: s.footerSource || "Information checked against the official Steam store page, the publisher and media reports.",
    quickAnswers: s.quickAnswers || "Quick answers", guides: s.guides || "All guides", aboutGame: s.aboutGame || "About the game",
    startPlaying: s.startPlaying || "Get it on Steam", getOnSteam: s.getOnSteam || "Get it on Steam ↗", readGuide: s.readGuide || "How to Play →",
    moreGuides: s.moreGuides || "More guides", sources: s.sources || "Sources & fact-checking",
    caseFile: s.caseFile || "CASE FILE", evidence: s.evidence || "EVIDENCE", sealed: s.sealed || "SEALED",
    latest: s.latest || "Latest guides", updated: s.updated || "Updated", explore: s.explore || "Explore the investigation",
  };
};

/* ================= SVG detective-tool icons ================= */
const SVG = {
  logo: '<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="#0c0e12" stroke="#f2a900" stroke-width="2.2"/><circle cx="20" cy="20" r="14.5" fill="none" stroke="#e63946" stroke-width="1" stroke-dasharray="3 3" opacity=".7"/><circle cx="17" cy="16" r="6" fill="none" stroke="#e8e6e1" stroke-width="2.4"/><path d="M21.6 20.6 27 26" stroke="#e8e6e1" stroke-width="2.4" stroke-linecap="round"/><path d="M12 12.5 8 8.5M13.5 9l-1.5-3M28 12.5 32 8.5" stroke="#e63946" stroke-width="1.4" stroke-linecap="round"/></svg>',
  "how-to-play": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M15.91 11.672a.375.375 0 010 .656l-5.603 3.113a.375.375 0 01-.557-.328V8.887c0-.286.307-.466.557-.327l5.603 3.112z"/></svg>',
  "walkthrough": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3m0 12v3M3 12h3m12 0h3M5.6 5.6l2.1 2.1m8.6 8.6 2.1 2.1m0-12.8-2.1 2.1M7.7 16.3l-2.1 2.1"/><circle cx="12" cy="12" r="3.2"/></svg>',
  "choices": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h7a3 3 0 013 3v11m0 0-3.5-3.5M14 19l3.5-3.5M8 5 4.5 8.5M8 5l3.5 3.5"/></svg>',
  "endings": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4 6.5 9.5 12 15l5.5-5.5L12 4z"/><path d="M6.5 9.5h11M8 15l1.5 5h5L16 15"/></svg>',
  "cases": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3.75 7.5 12 4l8.25 3.5L12 11 3.75 7.5z"/><path d="M3.75 12 12 15.5l8.25-3.5M3.75 16.5 12 20l8.25-3.5"/></svg>',
  "characters": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4.5 20c1.2-3.6 4-5.5 7.5-5.5s6.3 1.9 7.5 5.5"/><path d="M12 4v.5M8 5.5l.4.4M16 5.5l-.4.4"/></svg>',
  "investigation": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 11a1 1 0 100 2 1 1 0 000-2z"/><path d="M12 3a9 9 0 100 18 9 9 0 000-18z"/><path d="M12 6a6 6 0 100 12 6 6 0 000-12z" opacity=".55"/></svg>',
  "achievements": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="5.5"/><path d="M8.5 13.5 7 21l5-2.5L17 21l-1.5-7.5"/></svg>',
  "controls": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="7" width="19" height="10" rx="2.5"/><path d="M6.5 10.5v3M5 12h3M16 12h.01M18.5 10.5h.01M18.5 13.5h.01"/></svg>',
  "system-requirements": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M8 20h8m-4-3.5V20"/><path d="M7 8h4M7 11h7"/></svg>',
  "steam-deck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="6" width="16" height="12" rx="3"/><path d="M8.5 10h.01M12 10h.01M15.5 10h.01M9.5 13.5c.8.8 4.2.8 5 0"/></svg>',
  "tips-and-tricks": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6M10 21h4M12 3a6 6 0 00-3.6 10.8c.7.6 1.1 1.3 1.1 2.2h5c0-.9.4-1.6 1.1-2.2A6 6 0 0012 3z"/></svg>',
  "faq": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9.2a2.6 2.6 0 115.1.9c-.6 1.1-2.1 1.6-2.1 2.9M12 16.5h.01"/></svg>',
  "update-log": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 3h6"/></svg>',
  "where-to-buy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 14v3m0-9V5m-3 5h.008M9 10h.008M12 13h.008M15 13h.008M18 10h.008M6 10h.008M2.25 18.75L4.5 6.5A2.25 2.25 0 016.7 4.75h10.6a2.25 2.25 0 012.2 1.75l2.25 12.25M3 18.75h18a.75.75 0 01.75.75v1.5H2.25v-1.5a.75.75 0 01.75-.75z"/></svg>',
  "how-long-to-beat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>',
  "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5m-6 6 6-6 6 6"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a7 7 0 00-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 00-7-7zm0 9.5A2.5 2.5 0 1112 6a2.5 2.5 0 010 5.5z"/></svg>',
};

/* ---------- head ---------- */
function hreflang(slug){
  const hrefs = LANGS.map(l => `<link rel="alternate" hreflang="${LANG_META[l]?.html || l}" href="${urlOf(slug,l)}" />`).join("\n");
  return hrefs + `\n<link rel="alternate" hreflang="x-default" href="${urlOf(slug,DEF)}" />`;
}
function head(title, desc, extraLd, slug, lang, ogImage){
  const ld = JSON.stringify([siteLd(lang)].concat(extraLd || []));
  const gsc = DATA.site.gscVerification ? `<meta name="google-site-verification" content="${esc(DATA.site.gscVerification)}" />` : "";
  const og = ogImage || DATA.site.ogImage || "/images/hero.jpg";
  const htmlLang = LANG_META[lang]?.html || lang;
  return `<!DOCTYPE html>
<html lang="${htmlLang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}" />
<link rel="canonical" href="${urlOf(slug,lang)}" />
${hreflang(slug)}
<meta name="theme-color" content="#0c0e12" />
<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
${gsc}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="${esc(siteI18n(lang).name)}" />
<meta property="og:title" content="${esc(title)}" />
<meta property="og:description" content="${esc(desc)}" />
<meta property="og:url" content="${urlOf(slug,lang)}" />
<meta property="og:image" content="https://${DATA.site.domain}${og}" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800;900&family=Chakra+Petch:wght@600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/css/style.css?v=${CSS_V}" />${slug === "index" ? "\n" + KIT.heroPreload({ srcset: HERO_SET, sizes: "100vw" }) : ""}
<script type="application/ld+json">${ld}</script>
${DATA.site.gaId ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${esc(DATA.site.gaId)}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${esc(DATA.site.gaId)}');</script>` : ""}
</head>
<body>`;
}
function langSwitcher(lang, slug){
  const items = LANGS.map(l =>
    `<a href="${urlOf(slug,l)}" class="${l===lang?"active":""}"><span class="flag svg-flag">${flagOf(l)}</span>${LANG_META[l]?.name||l}</a>`
  ).join("");
  return `<details class="lang-dd">
    <summary><span class="flag svg-flag">${flagOf(lang)}</span><span class="lang-name">${LANG_META[lang]?.name||lang}</span><span class="caret">▾</span></summary>
    <div class="dd-menu dd-lang">${items}</div>
  </details>`;
}
function header(lang, active){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const guideItems = DATA.pages.map(p => {
    const m = metaOf(p.slug);
    return `<a href="${prefix}/${p.slug}" class="${p.slug===active?"active":""}"><span class="nav-ic">${SVG[m.icon]}</span><span>${esc(pageOf(p,lang).title)}</span></a>`;
  }).join("");
  return `<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="${prefix}/"><span class="logo-badge">${SVG.logo}</span><span class="logo-txt">${esc(s.name)}</span></a>
    <nav class="nav" aria-label="Main">
      <a href="${prefix}/" class="${active===""?"active":""}">${esc(s.navHome)}</a>
      <details class="dd">
        <summary>${esc(s.navGuides)} <span class="caret">▾</span></summary>
        <div class="dd-menu dd-grid">${guideItems}</div>
      </details>
      <a href="${prefix}/cases" class="${active==="cases"?"active":""}">${esc(s.navCases)}</a>
      <a href="${prefix}/characters" class="${active==="characters"?"active":""}">${esc(s.navCharacters)}</a>
    </nav>
    <form class="site-search" action="https://www.google.com/search" method="get" target="_blank" rel="noopener" role="search">
      <input type="search" name="q" placeholder="${lang==="en"?"Search guides…":lang==="ja"?"ガイドを検索…":lang==="ko"?"공략 검색…":"搜索攻略…"}" aria-label="${lang==="en"?"Search guides":lang==="ja"?"ガイドを検索":lang==="ko"?"공략 검색":"搜索攻略"}" />
      <input type="hidden" name="as_sitesearch" value="${esc(DATA.site.domain)}" />
      <span class="search-ic" aria-hidden="true">${SVG.logo.replace('<svg viewBox="0 0 40 40"','<svg viewBox="0 0 24 24"').replace('</svg>','<circle cx="11" cy="11" r="6" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>')}</span>
    </form>
    ${langSwitcher(lang, active || "index")}
  </div>
</header>`;
}
function footer(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const cols = DATA.pages.slice(0, 8).map(p => `<a href="${prefix}/${p.slug}">${esc(pageOf(p,lang).title)}</a>`).join("");
  return `<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand-row">
      <div class="footer-brand"><span class="logo-badge small">${SVG.logo}</span><span>${esc(s.name)}</span></div>
      <div class="footer-links">
        <a href="${prefix}/about">${esc(s.navAbout)}</a><a href="${prefix}/privacy">${esc(s.navPrivacy)}</a><a href="${prefix}/contact">${esc(s.navContact)}</a>
        <a href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">Steam ↗</a>
      </div>
    </div>
    <div class="footer-cols">
      <nav class="footer-col">${cols}</nav>
      <div class="footer-meta">
        <p>${esc(s.tagline)}</p>
        <p>${esc(s.footerNote)}</p>
        <p>${esc(s.footerSource)} · ${today}</p>
      </div>
    </div>
    ${DATA.site.adsenseId ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(DATA.site.adsenseId)}" crossorigin="anonymous"></script>` : ""}
  </div>
<script>
document.addEventListener('click', function(e){
  document.querySelectorAll('details.dd[open], details.lang-dd[open]').forEach(function(d){
    if (!d.contains(e.target)) d.removeAttribute('open');
  });
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Escape') document.querySelectorAll('details[open]').forEach(function(d){ d.removeAttribute('open'); });
});
document.addEventListener('DOMContentLoaded', function(){
  var obs = new IntersectionObserver(function(es){
    es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, {threshold:.08});
  document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length) {
    var tocTargets = tocLinks.map(function(a){ return document.querySelector(a.getAttribute('href')); });
    var tocObs = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if (en.isIntersecting) {
          var id = '#' + en.target.id;
          tocLinks.forEach(function(a){ a.classList.toggle('active', a.getAttribute('href') === id); });
        }
      });
    }, {rootMargin:'-15% 0px -70% 0px', threshold:0});
    tocTargets.forEach(function(s){ if (s) tocObs.observe(s); });
  }
});
</script>
</footer>
<a class="back-top" href="#" aria-label="Top">${SVG.up}</a>
</body></html>`;
}

/* ---------- sections ---------- */
let SEC_IDX = 0;
function secId(){ SEC_IDX += 1; return "sec-" + SEC_IDX; }
function renderSection(s, lang){
  const id = secId(s.heading);
  switch(s.type){
    case "steps": {
      // 讯问步骤：编号证据链（线索引）
      const items = (s.items||[]).map((it,i)=>`<li class="interrog-step"><span class="int-no">${String(i+1).padStart(2,"0")}</span><div><strong>${esc(Array.isArray(it)?it[0]:it)}</strong>${Array.isArray(it)&&it[1]?`<p>${esc(it[1])}</p>`:""}</div></li>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"INTERROG")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}<ol class="interrog">${items}</ol></section>`;
    }
    case "list": {
      // 线索清单：证据勾选项
      const items = (s.items||[]).map(it=>`<li class="lead-item"><span class="lead-box" aria-hidden="true"></span><p>${esc(it)}</p></li>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"LEADS")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}<ul class="lead-list">${items}</ul></section>`;
    }
    case "table": {
      // 档案表：斑驳纸面表格
      const headRow = (s.columns||[]).map(c=>`<th>${esc(c)}</th>`).join("");
      const rows = (s.rows||[]).map(r=>`<tr>${r.map(c=>`<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"FILE")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}<div class="file-table"><table><thead><tr>${headRow}</tr></thead><tbody>${rows}</tbody></table></div></section>`;
    }
    case "faq": {
      // 审问问答
      const items = (s.items||[]).map(([q,a])=>`<details class="interrog-faq"><summary>${esc(q)}<span class="pm">+</span></summary><div class="interrog-a">${esc(a)}</div></details>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"QA")}</span><h2>${esc(s.heading)}</h2></div>${items}</section>`;
    }
    case "evidence": {
      const items = (s.items||[]).map(([label,txt])=>`<div class="evidence"><span class="ev-tag">${esc(label)}</span><p>${esc(txt)}</p></div>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"EVIDENCE")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}<div class="evidence-stack">${items}</div></section>`;
    }
    case "timeline": {
      const items = (s.items||[]).map(([t,txt])=>`<li class="tl-item"><span class="tl-time">${esc(t)}</span><p>${esc(txt)}</p></li>`).join("");
      return `<section class="dossier-sheet reveal" id="${id}"><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"TIMELINE")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}<ul class="timeline">${items}</ul></section>`;
    }
    case "note": {
      // 案件便签（黄纸+图钉）
      return `<section class="dossier-sheet reveal case-note" id="${id}"><div class="case-pin" aria-hidden="true"></div><div class="sheet-head"><span class="sheet-tag">${esc(s.tag||"FIELD NOTE")}</span><h2>${esc(s.heading)}</h2></div>${s.body?`<p class="sheet-lead">${esc(s.body)}</p>`:""}</section>`;
    }
    default: return "";
  }
}
/* ---------- home ---------- */
function renderHome(lang){
  const s = siteI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const gname = (DATA.game.nameI18n && DATA.game.nameI18n[lang]) || DATA.game.name;
  const gintro = (DATA.game.introI18n && DATA.game.introI18n[lang]) || DATA.game.intro;
  const statsArr = (DATA.game.statsI18n && DATA.game.statsI18n[lang]) || DATA.game.stats || [];
  const stats = statsArr.map(st=>`<div class="stat"><b>${esc(st.value)}</b><span>${esc(st.label)}</span></div>`).join("");
  const _faqSec = (pageOf(DATA.pages.find(p=>p.slug==="faq"), lang).sections||[]).find(x=>x.type==="faq");
  const faqItems = _faqSec?.items || [];
  const faqHtml = faqItems.map(([q,a])=>`<details class="faq"><summary>${esc(q)}<span class="pm">+</span></summary><div class="faq-a">${esc(a)}</div></details>`).join("");
  const keyFactsArr = (DATA.game.keyFactsI18n && DATA.game.keyFactsI18n[lang]) || DATA.game.keyFacts || [];
  const keyFacts = keyFactsArr.map(f=>`<li>${esc(f)}</li>`).join("");
  // 证据分组：案件主线 / 深挖 / 答案
  const CORE = ["walkthrough","choices","endings","investigation","characters","cases"];
  const DEEP = ["evidence","controls","tips-and-tricks","system-requirements","steam-deck"];
  const ANS  = ["achievements","update-log","faq"];
  const evCard = (slug,i,type) => {
    const p=DATA.pages.find(x=>x.slug===slug); if(!p) return "";
    const m=metaOf(slug); const t=Object.assign(pageOf(p,lang),{slug:p.slug});
    return `<a class="ev-card reveal" data-type="${type}" href="${prefix}/${slug}">
      <span class="ev-id">${m.id||("C-"+String(i+1).padStart(2,"0"))}</span>
      <span class="ev-ic">${SVG[m.icon]}</span>
      <h3>${esc(t.title)}</h3>
      <p>${esc(t.metaDescription)}</p>
      <span class="ev-open">${esc(s.readGuide)}</span>
    </a>`;
  };
  const coreCards = CORE.map((sl,i)=>evCard(sl,i,"core")).join("");
  const deepCards = DEEP.map((sl,i)=>evCard(sl,i,"deep")).join("");
  const ansCards  = ANS.map((sl,i)=>evCard(sl,i,"ans")).join("");
  // 案件时间线（横向）
  const timeline = [
    [lang==="en"?"Day 1 — The Fall":lang==="ja"?"第1日——崩落":lang==="ko"?"1일차 — 추락":"第1天——坠落", lang==="en"?"The protagonist's past is buried in the medical gauge letter.":lang==="ja"?"主人公の過去は医療ゲージの手紙に埋もれている。":lang==="ko"?"주인공의 과거는 의료 게이지 편지에 묻혀 있습니다.":"主角的过去埋在医疗刻度表的信里。"],
    [lang==="en"?"The Shadow":lang==="ja"?"影":lang==="ko"?"그림자":"影子", lang==="en"?"Reconstruct the final moments of the dead.":lang==="ja"?"死者の最後の瞬間を再現する。":lang==="ko"?"죽은 자의 마지막 순간을 재구성합니다.":"还原死者最后的时刻。"],
    [lang==="en"?"Rewind Time":lang==="ja"?"時間を巻き戻す":lang==="ko"?"시간 되감기":"回溯时间", lang==="en"?"Every choice rewrites the truth in Dark Tide City.":lang==="ja"?"選択が暗潮市の真実を書き換える。":lang==="ko"?"선택이 다크 타이드 시티의 진실을 다시 씁니다.":"每次选择都改写暗潮市的真相。"],
    [lang==="en"?"Multiple Endings":lang==="ja"?"複数のエンディング":lang==="ko"?"다중 엔딩":"多重结局", lang==="en"?"Corruption meter decides how far you fall.":lang==="ja"?"汚染メーターがどこまで堕ちるかを決める。":lang==="ko"?"오염 게이지가 얼마나 떨어질지 결정합니다.":"腐化值决定你坠得多深。"],
  ].map(([t,d],i)=>`<div class="tl-card reveal"><span class="tl-no">${String(i+1).padStart(2,"0")}</span><b>${esc(t)}</b><p>${esc(d)}</p></div>`).join("");
  const heroImg="/images/hero.jpg";
  const badgeTxt = lang==="en" ? "A detective RPG with the dead's memories — updated regularly"
    : lang==="ja" ? "死者の記憶を追う刑事RPG — 定期更新"
    : lang==="ko" ? "죽은 자의 기억을 쫓는 추리 RPG — 정기 업데이트"
    : "追查死者记忆的侦探RPG — 持续更新";
  const h1Tail = lang==="en" ? "CASE FILES" : lang==="ja" ? "事件ファイル" : lang==="ko" ? "사건 파일" : "案件卷宗";
  const body = `
  <main>
    <section class="wall-hero">
      <div class="wall-bg">${KIT.picture({ src:"/images/hero-1280.jpg", srcset:HERO_SET, sizes:"100vw", attrs:`alt="${esc(gname)} key art" loading="eager" width="1600" height="900" fetchpriority="high"` })}</div>
      <div class="wall-overlay"></div>
      <div class="container wall-copy">
        <span class="evidence-tag"><span class="dot"></span> ${esc(badgeTxt)}</span>
        <h1>${esc(gname)} <span class="stamp-hl">${esc(h1Tail)}</span></h1>
        <p class="lead">${esc(s.tagline)}. ${esc(s.explore)}.</p>
        <div class="stats wall-stats">${stats}</div>
        <div class="cta-row">
          <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">${esc(s.startPlaying)}</a>
          <a class="btn btn-ghost" href="${prefix}/walkthrough">${esc(s.readGuide)}</a>
        </div>
      </div>
      <div class="wall-stamp" aria-hidden="true">${esc(s.sealed)}</div>
    </section>
    <section class="container section">
      <div class="sec-head reveal"><span class="mono">${esc(s.caseFile)} // TIMELINE</span><h2>${esc(lang==="en"?"The Investigation":lang==="ja"?"捜査の軌跡":lang==="ko"?"수사의 궤적":"调查轨迹")}</h2></div>
      <div class="tl-row">${timeline}</div>
    </section>
    <section class="container section">
      <div class="sec-head reveal"><span class="mono">${esc(s.caseFile)} // EVIDENCE WALL</span><h2>${esc(s.guides)}</h2></div>
      <div class="case-filters reveal">
        <button class="case-filter" data-filter="all" aria-pressed="true">${esc(lang==="en"?"All cases":lang==="ja"?"全事件":lang==="ko"?"전체 사건":"全部案件")}</button>
        <button class="case-filter" data-filter="core" aria-pressed="false">${esc(lang==="en"?"Main case":lang==="ja"?"本編":lang==="ko"?"본편":"主线案件")}</button>
        <button class="case-filter" data-filter="deep" aria-pressed="false">${esc(lang==="en"?"Deep dive":lang==="ja"?"深掘り":lang==="ko"?"심층":"深挖")}</button>
        <button class="case-filter" data-filter="ans" aria-pressed="false">${esc(lang==="en"?"Answers":lang==="ja"?"解答":lang==="ko"?"답변":"答案")}</button>
      </div>
      <div class="ev-wall ev-wall-all">${coreCards}${deepCards}${ansCards}</div>
    </section>
    <section class="container section split">
      <div class="card dossier reveal">
        <h2><span class="sec-tag">${esc(s.aboutGame)}</span>${esc(gname)}</h2>
        <p class="sec-body">${esc(gintro)}</p>
        <ul class="checks">${keyFacts}</ul>
      </div>
      <div class="card dossier reveal">
        <h2><span class="sec-tag">${esc(s.quickAnswers)}</span></h2>
        ${faqHtml}
      </div>
    </section>
  </main>
  <script>
  document.addEventListener('DOMContentLoaded', function(){
    var filters=document.querySelectorAll('.case-filter');
    var cards=document.querySelectorAll('.ev-card[data-type]');
    filters.forEach(function(f){
      f.addEventListener('click', function(){
        filters.forEach(function(x){x.setAttribute('aria-pressed','false');x.classList.remove('on');});
        f.setAttribute('aria-pressed','true');f.classList.add('on');
        var v=f.dataset.filter;
        cards.forEach(function(c){
          if(v==='all'||c.dataset.type===v){c.style.display='';}else{c.style.display='none';}
        });
      });
    });
  });
  </script>`;
  return renderFull(lang, siteI18n(lang).name, s.description, [], "index", body, heroImg);
}
function renderFull(lang, title, desc, extraLd, slug, body, ogImage){
  const s = siteI18n(lang);
  return head(title, desc, extraLd, slug, lang, ogImage) + header(lang, slug === "index" ? "" : slug) + body + footer(lang);
}

/* ---------- article pages ---------- */
function renderPage(lang, page){
  const t = Object.assign(pageOf(page, lang), {slug: page.slug});
  const prefix = lang === DEF ? "" : `/${lang}`;
  SEC_IDX = 0;
  const toc = (t.sections||[]).filter(x=>x.heading).map((x,i)=>{
    SEC_IDX += 1;
    return `<a href="#sec-${SEC_IDX}"><span class="evt-no">${String(SEC_IDX).padStart(2,"0")}</span>${esc(x.heading)}</a>`;
  }).join("");
  SEC_IDX = 0;
  const sections2 = (t.sections||[]).map(x => renderSection(x, lang)).join("");
  const related = DATA.pages.filter(p=>p.slug!==page.slug).slice(0,6).map(p=>{
    const m = metaOf(p.slug);
    return `<a href="${prefix}/${p.slug}"><span class="nav-ic">${SVG[m.icon]}</span><span>${esc(pageOf(p,lang).title)}</span></a>`;
  }).join("");
  const srcList = page.sources || [];
  const sources = srcList.map(x=>`<li>${AFF.anchor({ url: x.url, text: (x.labels && x.labels[lang]) || x.label, suffix: " ↗" })}</li>`).join("");
  // FTC：页面上只要有一条计佣链接就必须披露，且要显示在链接附近
  const affNote = AFF.needsDisclosure(srcList.map(x=>x.url))
    ? `<p class="aff-note">${esc(KIT.affiliateDisclosure(lang))}</p>` : "";
  const s = siteI18n(lang);
  const heroImg = t.heroImage;
  const srcsetOf = img => {
    if (!img) return null;
    const base = img.replace(/\.(jpg|jpeg|png|webp)$/i, "");
    return { srcset: `${base}-640.jpg 640w, ${base}-1280.jpg 1280w, ${img} 1600w`, sizes: "(max-width: 640px) 94vw, (max-width: 960px) 92vw, 820px" };
  };
  const pageHero = heroImg ? `<div class="dossier-hero-img">${KIT.picture({ ...srcsetOf(heroImg), src: heroImg, attrs: `alt="${esc(t.title)}" loading="lazy" width="1600" height="900"` })}</div>` : "";
  const noImgCls = heroImg ? "" : " noimg";
  const body = `
  <main class="container">
    <nav class="crumbs"><a href="${prefix}/">${esc(s.navHome)}</a><span>›</span><span>${esc(t.title)}</span></nav>
    <div class="file-open-hero reveal${noImgCls}">
      ${heroImg ? "" : `<span class="hero-ic" aria-hidden="true">${SVG[page.meta?.icon || "faq"]}</span>`}
      <span class="evidence-tag">${esc(s.caseFile)} // ${esc(page.meta?.id || page.slug.toUpperCase())}</span>
      <h1>${esc(t.title)}</h1>
      <p class="intro">${esc(t.intro)}</p>
      ${pageHero}
    </div>
    <div class="dossier-grid">
      <aside class="evidence-rail">
        ${toc ? `<nav class="toc reveal"><b class="toc-title">${esc(s.updated)}</b>${toc}</nav>` : ""}
        <div class="case-tag reveal">
          <span class="cm-tag">${esc(s.caseFile)}</span>
          <div class="cm-row"><span class="cm-k">${esc(lang==="en"?"Case No.":lang==="ja"?"事件番号":lang==="ko"?"사건 번호":"案件编号")}</span><b>${esc(page.meta?.id || page.slug.toUpperCase())}</b></div>
          <div class="cm-row"><span class="cm-k">${esc(lang==="en"?"Category":lang==="ja"?"分類":lang==="ko"?"분류":"分类")}</span><b>${esc(t.title.split(":")[0].split("—")[0].trim())}</b></div>
          <div class="cm-row"><span class="cm-k">${esc(s.updated)}</span><b>${today}</b></div>
          <div class="cm-stamp">${esc(s.sealed)}</div>
        </div>
        <div class="cta-box reveal">
          <span class="mono">${esc(s.caseFile)} // STEAM</span>
          <p>${esc(gnameOf(lang))}</p>
          <a class="btn btn-primary" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">${esc(s.getOnSteam)}</a>
        </div>
      </aside>
      <article class="dossier-main">
        ${sections2}
        ${sources ? `<div class="sources reveal"><b>${esc(s.sources)}</b><ul>${sources}</ul>${affNote}</div>` : ""}
        <div class="related reveal">
          <b>${esc(s.moreGuides)}</b>
          <div class="rel-grid">${related}</div>
        </div>
      </article>
    </div>
  </main>`;
  const extraLd = [articleLd(page, lang), breadcrumbLd(page, lang)];
  const fq = faqLd(t.sections);
  if (fq) extraLd.push(fq);
  return renderFull(lang, t.metaTitle || t.title, t.metaDescription, extraLd, page.slug, body, heroImg || DATA.site.ogImage);
}
function gnameOf(lang){ return (DATA.game.nameI18n && DATA.game.nameI18n[lang]) || DATA.game.name; }

/* ---------- static pages ---------- */
function renderStatic(lang, slug, title, body){
  const prefix = lang === DEF ? "" : `/${lang}`;
  const s = siteI18n(lang);
  const desc = KIT.staticDesc(slug, lang, s.name, title);
  return renderFull(lang, title, desc, [breadcrumbLd({slug,title}, lang)], slug, `<main class="container"><div class="article-wrap single"><article><div class="page-hero reveal"><span class="evidence-tag">${esc(s.caseFile)} // ${esc(slug.toUpperCase())}</span><h1>${esc(title)}</h1></div>${body}</article></div></main>`);
}
function genStatic(lang){
  const s = siteI18n(lang);
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  fs.mkdirSync(dir, {recursive:true});
  // about
  const aboutBody = `<section class="card dossier"><h2><span class="sec-tag">${esc(s.aboutTitle)}</span></h2><p class="sec-body">${
    lang==="ja" ? "このサイトは『キル・ザ・シャドウ』の非公式攻略サイトです。完全ウォークスルー、選択肢とエンディング、全事件、調査システム、キャラクター、FAQ をひとつの「事件ファイル」として整理しています。"
    : lang==="ko" ? "이 사이트는 『킬 더 섀도우』의 비공식 공략 사이트입니다. 완전 워크스루, 선택지와 엔딩, 모든 사건, 수사 시스템, 캐릭터, FAQ를 하나의 '사건 파일'로 정리했습니다."
    : "This is an unofficial fan guide site for Kill The Shadow. We organize the full walkthrough, choices and endings, every case, the investigation system, characters and FAQs into one 'case file'."
  }</p><ul class="checks"><li>${
    lang==="ja" ? "情報は Steam 公式ストアページ・パブリッシャー発表・信頼できるメディアで確認しています。"
    : lang==="ko" ? "정보는 Steam 공식 스토어 페이지, 퍼블리셔 발표, 신뢰할 수 있는 매체에서 확인했습니다."
    : "Facts are checked against the official Steam store page, publisher announcements and reputable media."
  }</li><li>${
    lang==="ja" ? "未確認の情報はその旨を明記しています。"
    : lang==="ko" ? "확인되지 않은 정보는 그렇게 표시합니다."
    : "Anything unverified is clearly marked as such."
  }</li><li>${
    lang==="ja" ? "このサイトは非公式であり、NEOWIZ・開発スタジオとは提携していません。"
    : lang==="ko" ? "이 사이트는 비공식이며 NEOWIZ·개발 스튜디오와 제휴하지 않았습니다."
    : "This site is unofficial and not affiliated with NEOWIZ or the developers."
  }</li></ul></section>`;
  writePage(path.join(dir,"about.html"), "about", lang, renderStatic(lang,"about",s.aboutTitle,aboutBody));
  // privacy
  const pBody = lang==="ja" ? `<p class="sec-body">このサイトはゲーム攻略サイトです。訪問者のプライバシーを尊重しています。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">収集する情報</h2><p>Google Analytics（GA4）で匿名のアクセス統計（ページビュー、流入元、端末タイプ、おおよその地域）を取得しています。氏名・メールアドレスなどの個人情報は収集しません。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookie</h2><p>Google Analytics はセッション統計のため Cookie を使用します。ブラウザで無効化できます。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">お問い合わせ</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p>`
    : lang==="ko" ? `<p class="sec-body">이 사이트는 게임 공략 사이트로, 방문자의 프라이버시를 존중합니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">수집 정보</h2><p>Google Analytics(GA4)로 익명의 접속 통계(페이지뷰, 유입 경로, 기기 유형, 대략적인 지역)를 수집합니다. 이름·이메일 등 개인정보는 수집하지 않습니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">쿠키</h2><p>Google Analytics는 세션 통계를 위해 쿠키를 사용합니다. 브라우저에서 비활성화할 수 있습니다.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">문의</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p>`
    : lang==="zh-TW" ? `<p class="sec-body">本網站為遊戲攻略網站，尊重訪客隱私。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">收集的資訊</h2><p>我們使用 Google Analytics（GA4）收集匿名流量統計：瀏覽量、來源、裝置類型與大致地區。我們不收集姓名、電子郵件等個人資料。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookie</h2><p>Google Analytics 會使用 Cookie 進行會話統計，可在瀏覽器中停用。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">聯絡</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p>`
    : lang==="zh-CN" ? `<p class="sec-body">本网站为游戏攻略网站，尊重访客隐私。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">收集的信息</h2><p>我们使用 Google Analytics（GA4）收集匿名流量统计：浏览量、来源、设备类型与大致地区。我们不收集姓名、邮箱等个人资料。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookie</h2><p>Google Analytics 会使用 Cookie 进行会话统计，可在浏览器中停用。</p><h2 style="font-size:1.05rem;margin:18px 0 8px">联系</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p>`
    : `<p class="sec-body">This is a game guide website and we respect visitor privacy.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">What we collect</h2><p>We use Google Analytics (GA4) for anonymous traffic statistics: page views, referrers, device types and approximate regions. We do not collect names, email addresses or any personally identifiable information.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Cookies</h2><p>Google Analytics sets cookies for session statistics. You can disable cookies in your browser.</p><h2 style="font-size:1.05rem;margin:18px 0 8px">Contact</h2><p><a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p>`;
  writePage(path.join(dir,"privacy.html"), "privacy", lang, renderStatic(lang,"privacy",s.privacyTitle,pBody));
  // contact
  const cBody = lang==="ja" ? `<p class="sec-body">お問い合わせ：<a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p style="margin-top:10px">通常 2〜3 営業日以内に返信します。</p>`
    : lang==="ko" ? `<p class="sec-body">문의：<a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p style="margin-top:10px">보통 2~3 영업일 이내에 답변합니다.</p>`
    : `<p class="sec-body">${lang==="zh-TW"?"聯絡我們：":lang==="zh-CN"?"联系我们：":"Reach us at:"} <a href="mailto:contact@${esc(DATA.site.domain)}">contact@${esc(DATA.site.domain)}</a></p><p style="margin-top:10px">${lang==="zh-TW"?"我們通常會在 2-3 個工作天內回覆。":lang==="zh-CN"?"我们通常会在 2-3 个工作日内回复。":"We usually reply within 2-3 business days."}</p>`;
  writePage(path.join(dir,"contact.html"), "contact", lang, renderStatic(lang,"contact",s.contactTitle,cBody));
}
function gen404(){
  const s = siteI18n(DEF);
  const list = DATA.pages.slice(0,6).map(p=>`<a class="btn btn-ghost" href="/${p.slug}">${esc(pageOf(p,DEF).title)}</a>`).join("");
  const body = `<main class="container" style="padding-top:60px;text-align:center"><section class="card dossier" style="max-width:600px;margin:0 auto"><span class="evidence-tag">ERROR // 404</span><h1>${esc(s.navHome)} — 404</h1><p style="margin:12px 0 20px">${esc(DEF==="en"?"The page you are looking for does not exist. Open a case file instead:":"ページが見つかりません。事件ファイルを開いてください。")}</p><div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">${list}</div></section></main>`;
  fs.writeFileSync(path.join(OUT,"404.html"), `<!DOCTYPE html><html lang="${LANG_META[DEF].html}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 — Not Found</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/css/style.css?v=${CSS_V}"></head><body>${header(DEF,"")}${body}${footer(DEF)}</body></html>`);
}

/* ---------- JSON-LD ---------- */
const siteLd = lang => ({"@context":"https://schema.org","@type":"WebSite",name:siteI18n(lang).name,url:urlOf("index",lang),description:siteI18n(lang).description});
function isoDate(str){
  const m=/([A-Za-z]+) (\d+), (\d+)/.exec(str||"")||[];
  const mo={Jan:1,Feb:2,Mar:3,Apr:4,May:5,Jun:6,Jul:7,Aug:8,Sep:9,Oct:10,Nov:11,Dec:12,January:1,February:2,March:3,April:4,May:5,June:6,July:7,August:8,September:9,October:10,November:11,December:12};
  return m[3] ? `${m[3]}-${String(mo[m[1]]||0).padStart(2,"0")}-${String(m[2]).padStart(2,"0")}` : today;
}
function gameLd(){
  return {"@context":"https://schema.org","@type":"VideoGame",name:DATA.game.name,description:DATA.game.intro,url:DATA.game.steamUrl,applicationCategory:"Game",operatingSystem:"Windows",genre:DATA.game.genre,datePublished:isoDate(DATA.game.releaseDate),inLanguage:"en",offers:{"@type":"Offer",price:DATA.game.price,priceCurrency:"USD",availability:"https://schema.org/InStock"}};
}
function articleLd(page, lang){
  const t = pageOf(page, lang);
  return {"@context":"https://schema.org","@type":"Article",headline:t.title,description:t.metaDescription,mainEntityOfPage:urlOf(page.slug,lang),datePublished:DATA.game.releaseDate||today,dateModified:KIT.LASTMOD_TOKEN,inLanguage:LANG_META[lang]?.html||lang,publisher:{"@type":"Organization",name:siteI18n(lang).name}};
}
function faqLd(sections){
  const items = (sections||[]).filter(s=>s.type==="faq").flatMap(s=>s.items||[]);
  if (!items.length) return null;
  return {"@context":"https://schema.org","@type":"FAQPage",mainEntity:items.map(([q,a])=>({"@type":"Question",name:q,acceptedAnswer:{"@type":"Answer",text:a}}))};
}
function breadcrumbLd(page, lang){
  return {"@context":"https://schema.org","@type":"BreadcrumbList",itemListElement:[{"@type":"ListItem",position:1,name:siteI18n(lang).navHome,item:`https://${DATA.site.domain}/${lang===DEF?"":lang+"/"}`},{"@type":"ListItem",position:2,name:page.title,item:urlOf(page.slug,lang)}]};
}

/* ---------- build ---------- */
// 写页面统一走这里：按「内容是否真变了」把 lastmod 占位符换成真实日期
const writePage = (filePath, slug, lang, html) => fs.writeFileSync(filePath, LM.stamp(urlOf(slug, lang), html));
fs.rmSync(OUT, {recursive:true, force:true});
fs.mkdirSync(OUT, {recursive:true});
// assets copy
for (const f of ["favicon.svg","favicon-16x16.png","favicon-32x32.png","apple-touch-icon.png"]) {
  const src = path.join(ROOT,"assets","favicon",f);
  if (fs.existsSync(src)) fs.copyFileSync(src, path.join(OUT,f));
}
const imgDir = path.join(ROOT,"assets","images");
if (fs.existsSync(imgDir)) {
  fs.mkdirSync(path.join(OUT,"images"),{recursive:true});
  for (const f of fs.readdirSync(imgDir)) {
    if (/\.(jpg|jpeg|webp)$/i.test(f)) fs.copyFileSync(path.join(imgDir,f), path.join(OUT,"images",f));
  }
}
fs.mkdirSync(path.join(OUT,"css"),{recursive:true});
fs.writeFileSync(path.join(OUT,"css","style.css"), fs.readFileSync(path.join(ROOT,"templates","style.css"),"utf8"));

// index + pages per language
for (const lang of LANGS) {
  const dir = path.join(OUT, lang === DEF ? "" : lang);
  fs.mkdirSync(dir, {recursive:true});
  writePage(path.join(dir,"index.html"), "index", lang, renderHome(lang));
  for (const page of DATA.pages) {
    SEC_IDX = 0;
    const html = renderPage(lang, page);
    writePage(path.join(dir, page.slug + ".html"), page.slug, lang, html);
  }
  genStatic(lang);
}
gen404();

// sitemap（lastmod 走 LM：内容没变就沿用旧日期，不再每次全站标记为当天）
const urls = [];
for (const lang of LANGS) {
  urls.push({ loc: urlOf("index",lang), priority: "1.0" });
  for (const p of DATA.pages) urls.push({ loc: urlOf(p.slug,lang), priority: "0.8" });
  for (const sp of ["about","privacy","contact"]) urls.push({ loc: urlOf(sp,lang), priority: "0.3" });
}
const smN = KIT.writeSitemap(OUT, urls, LM);
KIT.writeRobots(OUT, DATA.site.domain);
KIT.writeAds(OUT, DATA.site.adsenseId);
KIT.writeHeaders(OUT);
KIT.writeIndexNowKey(OUT, DATA.site.indexNowKey);
// llms.txt：给 AI agent 的机器可读入口（不是 SEO 手段，见 site-kit 注释）
KIT.writeLlmsTxt(OUT, {
  siteName: DATA.site.name,
  domain: DATA.site.domain,
  summary: `Unofficial ${DATA.game.name} guide site. Each page answers one question players actually search for, and lists the sources it was checked against. Available in ${LANGS.length} languages: ${LANGS.join(", ")}.`,
  pages: DATA.pages.map(p => { const t = pageOf(p, DEF); return { slug: p.slug, title: t.title, desc: t.metaDescription }; }),
  notes: [
    "Facts are checked against the official Steam store page and reputable gaming media; every page lists its own sources at the bottom.",
    "Anything we could not verify is explicitly marked as unverified — gaps are left open rather than filled with generated text.",
    "Localised versions live under /<lang>/ (e.g. /ja/how-to-play) and are declared via hreflang on every page.",
    "This is an unofficial fan site, not affiliated with the game's developer or publisher."
  ]
});
const lm = LM.save();
console.log(`✓ ${LANGS.length} locales × ${1+DATA.pages.length+3} pages｜sitemap ${smN} URL｜内容有变更 ${lm.changed}/${lm.total} 页`);
