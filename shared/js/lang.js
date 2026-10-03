(() => {
  const KEY = "ed-lang";
  const params = new URLSearchParams(location.search);
  const q = params.get("lang");
  let lang = q === "en" || q === "ru" ? q : localStorage.getItem(KEY) || "ru";
  if (q === "en" || q === "ru") {
    try {
      localStorage.setItem(KEY, q);
    } catch (_) {
      /* ignore */
    }
  }

  function setLang(next) {
    if (next !== "en" && next !== "ru") return;
    try {
      localStorage.setItem(KEY, next);
    } catch (_) {
      /* ignore */
    }
    const url = new URL(location.href);
    url.searchParams.set("lang", next);
    location.href = url.pathname + url.search + url.hash;
  }

  function withLang(href) {
    try {
      const u = new URL(href, location.href);
      u.searchParams.set("lang", lang);
      return u.pathname + u.search + (u.hash || "");
    } catch (_) {
      return href;
    }
  }

  function bind() {
    document.querySelectorAll("[data-set-lang]").forEach((btn) => {
      const next = btn.getAttribute("data-set-lang");
      btn.setAttribute("aria-pressed", String(next === lang));
      btn.addEventListener("click", () => setLang(next));
    });
    document.documentElement.lang = lang;
    document.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (!href || href.startsWith("#") || href.startsWith("http") || href.startsWith("mailto:")) return;
      if (href.includes("lang=")) return;
      a.setAttribute("href", withLang(href));
    });
  }

  window.ED_LANG = { lang, setLang, withLang, bind };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
