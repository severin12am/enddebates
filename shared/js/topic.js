(() => {
  const lang = (window.ED_LANG && window.ED_LANG.lang) || "en";
  const data =
    (lang === "ru" && window.TOPIC_DATA_RU) ||
    window.TOPIC_DATA_EN ||
    window.TOPIC_DATA;
  if (!data) return;

  const $ = (id) => document.getElementById(id);
  const ui = data.meta.ui || {};
  const t = (key, fallback) => (ui[key] != null && ui[key] !== "" ? ui[key] : fallback);

  if (data.meta.lang) document.documentElement.lang = data.meta.lang;
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (ui[key]) el.textContent = ui[key];
  });
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (ui[key]) el.setAttribute("placeholder", ui[key]);
  });

  function clockToSeconds(t) {
    const parts = String(t || "")
      .split(":")
      .map((x) => parseInt(x, 10));
    if (!parts.length || parts.some((n) => Number.isNaN(n))) return 0;
    if (parts.length === 3) return parts[0] * 3600 + parts[1] * 60 + parts[2];
    if (parts.length === 2) return parts[0] * 60 + parts[1];
    return parts[0];
  }

  function youtubeWatchUrl(links) {
    for (const l of links || []) {
      const u = (l && l.url) || "";
      const m = u.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([\w-]{11})/);
      if (m) return "https://www.youtube.com/watch?v=" + m[1];
    }
    return "";
  }
  const labels = data.meta.labels || {
    christian: "Christian case",
    muslim: "Muslim case",
  };

  $("title").textContent = data.meta.title;
  document.title = "EndDebates — " + data.meta.title;
  $("thesis").textContent = data.meta.thesis;
  if ($("purpose")) {
    if (data.meta.purpose) $("purpose").textContent = data.meta.purpose;
    else $("purpose").hidden = true;
  }
  if ($("warning")) {
    if (data.meta.warning) $("warning").textContent = data.meta.warning;
    else $("warning").hidden = true;
  }

  const chips = $("chips");
  (data.meta.chips || []).forEach((c) => {
    const s = document.createElement("span");
    s.className = "chip";
    s.textContent = c;
    chips.appendChild(s);
  });

  // Tabs
  const tabs = document.querySelectorAll("[data-tab]");
  const panels = document.querySelectorAll("[data-panel]");
  const available = new Set(
    ["live", "speech", "proofs", "verses", "brief", "arguments", "materials", "debates", "cards", "sources", "checklist"].filter(
      (id) => {
        if (id === "live") return true;
        if (id === "speech") return !!(data.opening_speech && (data.opening_speech.paragraphs || []).length);
        if (id === "proofs") return (data.trinity_proofs || []).length;
        if (id === "verses") return (data.verse_catalog || []).length;
        if (id === "materials") return (data.materials || []).length;
        if (id === "debates") return (data.debates || []).length;
        if (id === "arguments") return (data.arguments || []).length;
        if (id === "cards") return (data.opponent_cards || []).length;
        if (id === "sources") return (data.bibliography || []).length;
        if (id === "checklist") return (data.checklist || []).length;
        return true;
      }
    )
  );
  tabs.forEach((btn) => {
    if (!available.has(btn.dataset.tab)) {
      btn.hidden = true;
      return;
    }
    btn.addEventListener("click", () => {
      tabs.forEach((b) => b.setAttribute("aria-selected", String(b === btn)));
      panels.forEach((p) => p.classList.toggle("active", p.dataset.panel === btn.dataset.tab));
      history.replaceState(null, "", "#" + btn.dataset.tab);
    });
  });
  const initial = location.hash.replace("#", "") || data.meta.default_tab || "brief";
  const start =
    document.querySelector(`[data-tab="${initial}"]:not([hidden])`) ||
    document.querySelector("[data-tab]:not([hidden])");
  if (start) start.click();

  function receipts(items) {
    const ul = document.createElement("ul");
    ul.className = "receipts";
    (items || []).forEach((r) => {
      const li = document.createElement("li");
      if (r.url) {
        const a = document.createElement("a");
        a.href = r.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = r.label;
        li.appendChild(a);
        if (r.note) {
          const n = document.createElement("div");
          n.style.color = "var(--muted)";
          n.textContent = r.note;
          li.appendChild(n);
        }
      } else {
        li.textContent = r.label || r;
      }
      ul.appendChild(li);
    });
    return ul;
  }

  function quotesBlock(quotes) {
    if (!quotes || !quotes.length) return null;
    const wrap = document.createElement("div");
    quotes.forEach((q) => {
      const bq = document.createElement("blockquote");
      bq.className = "quote";
      const p = document.createElement("p");
      p.textContent = "“" + q.text + "”";
      bq.appendChild(p);
      if (q.orig) {
        const orig = document.createElement("p");
        orig.className = "orig";
        orig.textContent = q.orig;
        bq.appendChild(orig);
      }
      if (q.gloss) {
        const gloss = document.createElement("p");
        gloss.className = "gloss";
        gloss.textContent = q.gloss;
        bq.appendChild(gloss);
      }
      const who = document.createElement("div");
      who.className = "who";
      const parts = [q.who, q.work].filter(Boolean);
      who.textContent = parts.join(" — ");
      bq.appendChild(who);
      if (q.url) {
        const a = document.createElement("a");
        a.href = q.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = t("source", "source");
        a.style.fontFamily = "var(--font-ui)";
        a.style.fontSize = "0.75rem";
        bq.appendChild(a);
      }
      const copy = document.createElement("button");
      copy.type = "button";
      copy.className = "copy-btn";
      copy.textContent = t("copy", "Copy");
      copy.addEventListener("click", (e) => {
        e.stopPropagation();
        const line = "“" + q.text + "” — " + [q.who, q.work].filter(Boolean).join(", ");
        navigator.clipboard.writeText(line).then(() => {
          copy.textContent = t("copied", "Copied");
          setTimeout(() => (copy.textContent = t("copy", "Copy")), 1200);
        });
      });
      bq.appendChild(copy);
      wrap.appendChild(bq);
    });
    return wrap;
  }

  function listBox(title, items, kind) {
    if (!items || !items.length) return null;
    const box = document.createElement("div");
    box.className = kind === "mss" ? "mss-box" : "data-box";
    const lab = document.createElement("div");
    lab.className = "label";
    lab.textContent = title;
    box.appendChild(lab);
    const ul = document.createElement("ul");
    ul.className = "list-clean";
    items.forEach((item) => {
      const li = document.createElement("li");
      if (typeof item === "string") {
        li.textContent = item;
      } else if (item.url) {
        const a = document.createElement("a");
        a.href = item.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = item.label || item.fact || item.title;
        li.appendChild(a);
        const extra = item.note || item.fact;
        if (extra && extra !== a.textContent) {
          li.appendChild(document.createTextNode(" — " + extra));
        }
      } else {
        li.textContent = item.fact || item.label || JSON.stringify(item);
        if (item.source) li.appendChild(document.createTextNode(" (" + item.source + ")"));
      }
      ul.appendChild(li);
    });
    box.appendChild(ul);
    return box;
  }

  function sideBlock(kind, side) {
    const div = document.createElement("section");
    div.className = `side ${kind}`;
    const label = document.createElement("div");
    label.className = "label";
    label.textContent = labels[kind] || kind;
    const claim = document.createElement("p");
    claim.className = "claim";
    claim.textContent = side.claim;
    const caseP = document.createElement("p");
    caseP.className = "case";
    caseP.textContent = side.case;
    div.append(label, claim, caseP);
    const q = quotesBlock(side.quotes);
    if (q) div.appendChild(q);
    const data = listBox(t("data_points", "Data points"), side.data_points, "data");
    if (data) div.appendChild(data);
    const mss = listBox(t("manuscripts", "Manuscripts / artifacts"), side.manuscripts, "mss");
    if (mss) div.appendChild(mss);
    div.appendChild(receipts(side.sources || side.receipts || []));
    return div;
  }

  // Definitions
  const defs = $("defs");
  if (defs) {
    (data.definitions || []).forEach((d) => {
      const el = document.createElement("article");
      el.className = "def";
      el.innerHTML = `<h3>${d.term}</h3><p class="prose">${d.precise}</p>`;
      if (d.not) {
        const n = document.createElement("p");
        n.className = "not";
        n.textContent = d.not;
        el.appendChild(n);
      }
      defs.appendChild(el);
    });
  }

  // Positive cases
  const pillars = $("pillars");
  if (pillars && data.positive_cases) {
    Object.entries(data.positive_cases).forEach(([title, items]) => {
      const card = document.createElement("article");
      card.className = "card-static";
      card.innerHTML = `<h3>${title.replace(/_/g, " ")}</h3>`;
      const ul = document.createElement("ul");
      ul.className = "list-clean";
      items.forEach((t) => {
        const li = document.createElement("li");
        li.textContent = t;
        ul.appendChild(li);
      });
      card.appendChild(ul);
      pillars.appendChild(card);
    });
  }

  const speechEl = $("speech");
  if (speechEl && data.opening_speech) {
    const sp = data.opening_speech;
    const h = document.createElement("h2");
    h.textContent = sp.title || t("tab_speech", "Opening speech");
    speechEl.appendChild(h);
    if (sp.lede) {
      const lede = document.createElement("p");
      lede.className = "lede";
      lede.textContent = sp.lede;
      speechEl.appendChild(lede);
    }
    const fullText = [];
    (sp.paragraphs || []).forEach((block) => {
      const wrap = document.createElement("div");
      wrap.className = "speech-p";
      const p = document.createElement("p");
      p.textContent = block.text || "";
      wrap.appendChild(p);
      if (block.text) fullText.push(block.text);
      if (block.refs && block.refs.length) {
        const refs = document.createElement("div");
        refs.className = "speech-refs";
        block.refs.forEach((r) => {
          const a = document.createElement("a");
          a.href = r.url;
          a.target = "_blank";
          a.rel = "noopener noreferrer";
          a.textContent = r.ref;
          refs.appendChild(a);
        });
        wrap.appendChild(refs);
      }
      speechEl.appendChild(wrap);
    });
    const copyBtn = $("copy-speech");
    if (copyBtn) {
      copyBtn.addEventListener("click", () => {
        navigator.clipboard.writeText(fullText.join("\n\n")).then(() => {
          copyBtn.textContent = t("speech_copied", t("copied", "Copied"));
          setTimeout(() => (copyBtn.textContent = t("copy_speech", "Copy whole speech")), 1400);
        });
      });
    }
  }

  function appendVerseList(parent, verses) {
    if (!verses || !verses.length) return;
    const ul = document.createElement("ul");
    ul.className = "verse-list";
    verses.forEach((v) => {
      const li = document.createElement("li");
      li.className = "verse-row";
      const a = document.createElement("a");
      a.href = v.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = v.ref;
      li.appendChild(a);
      if (v.url_en) {
        const en = document.createElement("a");
        en.href = v.url_en;
        en.target = "_blank";
        en.rel = "noopener noreferrer";
        en.className = "verse-en";
        en.textContent = t("open_nrsv", "NRSV");
        li.appendChild(document.createTextNode(" "));
        li.appendChild(en);
      }
      if (v.hook) {
        const hook = document.createElement("div");
        hook.className = "verse-hook";
        hook.textContent = v.hook;
        li.appendChild(hook);
      }
      ul.appendChild(li);
    });
    parent.appendChild(ul);
  }

  const proofsEl = $("proofs");
  if (proofsEl && (data.trinity_proofs || []).length) {
    data.trinity_proofs.forEach((p, i) => {
      const details = document.createElement("details");
      details.className = "card";
      if (i < 2) details.open = true;
      const summary = document.createElement("summary");
      summary.innerHTML = `
        <div class="meta-line">
          ${p.hook ? `<span>${p.hook}</span>` : ""}
          ${p.pattern ? `<span>${p.pattern}</span>` : ""}
        </div>
        <h2>${p.they_say || p.hook || ""}</h2>`;
      const body = document.createElement("div");
      body.className = "body";
      const two = document.createElement("div");
      two.className = "two";
      const they = document.createElement("section");
      they.className = "side christian";
      they.innerHTML = `<div class="label">${t("they_claim_label", "Their case")}</div>`;
      const theyClaim = document.createElement("p");
      theyClaim.className = "claim";
      theyClaim.textContent = p.they_claim || "";
      they.appendChild(theyClaim);
      const theyQ = quotesBlock(p.they_quotes);
      if (theyQ) they.appendChild(theyQ);
      two.appendChild(they);
      const ans = document.createElement("section");
      ans.className = "side muslim";
      ans.innerHTML = `<div class="label">${t("counter_label", "Counter")}</div>`;
      const ansClaim = document.createElement("p");
      ansClaim.className = "claim";
      ansClaim.textContent = p.counter || "";
      ans.appendChild(ansClaim);
      const ansQ = quotesBlock(p.counter_quotes);
      if (ansQ) ans.appendChild(ansQ);
      const copy = document.createElement("button");
      copy.type = "button";
      copy.className = "copy-btn";
      copy.textContent = t("copy", "Copy");
      copy.addEventListener("click", (e) => {
        e.stopPropagation();
        navigator.clipboard.writeText(p.counter || "").then(() => {
          copy.textContent = t("copied", "Copied");
          setTimeout(() => (copy.textContent = t("copy", "Copy")), 1200);
        });
      });
      ans.appendChild(copy);
      two.appendChild(ans);
      body.appendChild(two);
      if (p.steelman) {
        const steel = document.createElement("div");
        steel.className = "note";
        const strong = document.createElement("strong");
        strong.textContent = t("steelman_label", "How they defend the verse") + ": ";
        steel.appendChild(strong);
        steel.appendChild(document.createTextNode(p.steelman));
        body.appendChild(steel);
      }
      appendVerseList(body, p.verses);
      details.append(summary, body);
      proofsEl.appendChild(details);
    });
    const expandP = $("expand-proofs");
    const collapseP = $("collapse-proofs");
    if (expandP) expandP.addEventListener("click", () => proofsEl.querySelectorAll("details").forEach((d) => (d.open = true)));
    if (collapseP) collapseP.addEventListener("click", () => proofsEl.querySelectorAll("details").forEach((d) => (d.open = false)));
  }

  // Arguments
  const argsEl = $("arguments");
  const filter = $("arg-filter");
  if (argsEl) {
    const clusters = [...new Set((data.arguments || []).map((a) => a.cluster).filter(Boolean))];
    if (filter) {
      clusters.forEach((c) => {
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        filter.appendChild(opt);
      });
    }
    function renderArgs(cluster) {
      argsEl.innerHTML = "";
      (data.arguments || [])
        .filter((a) => {
          if (!cluster || cluster === "all") return true;
          if (cluster === "top10") return a.importance === "Top 10" || (a.rank != null && a.rank >= 1 && a.rank <= 10);
          return a.cluster === cluster;
        })
        .forEach((arg) => {
          const details = document.createElement("details");
          details.className = "card";
          const summary = document.createElement("summary");
          const topTag = arg.importance || (arg.rank != null && arg.rank <= 10 ? "Top 10" : "");
          summary.innerHTML = `
            <div class="meta-line">
              ${arg.rank != null ? `<span>#${arg.rank}</span>` : ""}
              ${topTag ? `<span>${topTag}</span>` : ""}
              ${arg.cluster ? `<span>${arg.cluster}</span>` : ""}
              ${arg.type ? `<span>${arg.type}</span>` : ""}
              ${arg.popularity ? `<span>${arg.popularity}</span>` : ""}
            </div>
            <h2>${arg.title}</h2>`;
          const body = document.createElement("div");
          body.className = "body";
          if (arg.why_it_matters) {
            const why = document.createElement("p");
            why.className = "why";
            why.textContent = arg.why_it_matters;
            body.appendChild(why);
          }
          const two = document.createElement("div");
          two.className = "two";
          const keys = data.meta.side_keys || ["christian", "muslim"];
          const cSide = arg[keys[0]] || arg.christian || arg.bible_case;
          const mSide = arg[keys[1]] || arg.muslim || arg.quran_case;
          if (cSide) two.appendChild(sideBlock(keys[0], cSide));
          if (mSide) two.appendChild(sideBlock(keys[1], mSide));
          body.appendChild(two);
          const nested = arg.counters || arg.nested_counters;
          if (nested && nested.length) {
            const stack = document.createElement("div");
            stack.className = "counter-stack";
            nested.forEach((c) => {
              const card = document.createElement("div");
              card.className = "counter-card";
              const ag = document.createElement("div");
              ag.className = "against";
              ag.textContent = t("counter", "Counter → ") + (c.against || c.attacks || t("claim", "claim"));
              const p = document.createElement("p");
              p.className = "prose";
              p.innerHTML = "";
              const strong = document.createElement("strong");
              strong.textContent = c.claim || "";
              p.appendChild(strong);
              if (c.reply) {
                p.appendChild(document.createTextNode(" " + t("reply", "Reply: ") + c.reply));
              }
              card.append(ag, p);
              const qq = quotesBlock(c.quotes);
              if (qq) card.appendChild(qq);
              if (c.sources) card.appendChild(receipts(c.sources));
              stack.appendChild(card);
            });
            body.appendChild(stack);
          } else if (arg.counter_to_christian || arg.counter_to_muslim || arg.counter_to_bible || arg.counter_to_quran) {
            const counters = document.createElement("div");
            counters.className = "two";
            counters.innerHTML = `
              <div class="note"><strong>${t("counter_christian", "Counter (Christian):")}</strong> ${arg.counter_to_christian || arg.counter_to_bible || ""}</div>
              <div class="note"><strong>${t("counter_muslim", "Counter (Muslim):")}</strong> ${arg.counter_to_muslim || arg.counter_to_quran || ""}</div>`;
            body.appendChild(counters);
          }
          if (arg.live || arg.live_lines) {
            const live = arg.live || arg.live_lines;
            const box = document.createElement("dl");
            box.className = "live-box";
            const rows = [
              [t("if_they_say", "If they say"), live.if_they_say],
              [t("you_say", "You say"), live.you_say],
              [t("dont_overclaim", "Do not overclaim"), live.dont_overclaim],
            ];
            rows.forEach(([k, v]) => {
              if (!v) return;
              const dt = document.createElement("dt");
              dt.textContent = k;
              const dd = document.createElement("dd");
              dd.textContent = v;
              box.append(dt, dd);
            });
            body.appendChild(box);
          }
          if (arg.crux) {
            const crux = document.createElement("div");
            crux.className = "crux";
            crux.textContent = t("crux", "Crux: ") + arg.crux;
            body.appendChild(crux);
          }
          if (arg.debate_use) {
            const use = document.createElement("div");
            use.className = "use";
            use.textContent = t("debate_use", "Debate use: ") + arg.debate_use;
            body.appendChild(use);
          }
          details.append(summary, body);
          argsEl.appendChild(details);
        });
    }
    if (filter) filter.addEventListener("change", () => renderArgs(filter.value));
    const expand = $("expand-args");
    const collapse = $("collapse-args");
    if (expand) expand.addEventListener("click", () => argsEl.querySelectorAll("details").forEach((d) => (d.open = true)));
    if (collapse) collapse.addEventListener("click", () => argsEl.querySelectorAll("details").forEach((d) => (d.open = false)));
    renderArgs("all");
  }

  const versesEl = $("verses");
  if (versesEl && data.verse_catalog) {
    data.verse_catalog.forEach((g, i) => {
      const details = document.createElement("details");
      details.className = "card";
      if (i === 0) details.open = true;
      const summary = document.createElement("summary");
      summary.innerHTML = `
        <div class="meta-line">
          <span>${g.count || (g.verses || []).length} ${t("verses_count_suffix", "verses")}</span>
        </div>
        <h2>${g.title}</h2>`;
      const body = document.createElement("div");
      body.className = "body";
      if (g.move || g.uthman) {
        const u = document.createElement("div");
        u.className = "note";
        const strong = document.createElement("strong");
        strong.textContent = t("unitarian_move", "Why Jesus is not God: ");
        u.appendChild(strong);
        u.appendChild(document.createTextNode(" " + (g.move || g.uthman)));
        body.appendChild(u);
      }
      if (g.christian) {
        const c = document.createElement("div");
        c.className = "note";
        const strong = document.createElement("strong");
        strong.textContent = t("christian_reply", "Reply for the Trinity: ");
        c.appendChild(strong);
        c.appendChild(document.createTextNode(" " + g.christian));
        body.appendChild(c);
      }
      const ul = document.createElement("ul");
      ul.className = "verse-list";
      (g.verses || []).forEach((v) => {
        const li = document.createElement("li");
        li.className = "verse-row";
        const a = document.createElement("a");
        a.href = v.url;
        a.target = "_blank";
        a.rel = "noopener noreferrer";
        a.textContent = v.ref;
        li.appendChild(a);
        if (v.url_en) {
          const en = document.createElement("a");
          en.href = v.url_en;
          en.target = "_blank";
          en.rel = "noopener noreferrer";
          en.className = "verse-en";
          en.textContent = t("open_nrsv", "NRSV");
          li.appendChild(document.createTextNode(" "));
          li.appendChild(en);
        }
        if (v.hook) {
          const hook = document.createElement("div");
          hook.className = "verse-hook";
          hook.textContent = v.hook;
          li.appendChild(hook);
        }
        ul.appendChild(li);
      });
      body.appendChild(ul);
      details.append(summary, body);
      versesEl.appendChild(details);
    });
  }

  function materialCard(m, compact) {
    const art = document.createElement("article");
    art.className = "material";
    if (m.image) {
      const img = document.createElement("img");
      img.src = m.image;
      img.alt = m.title;
      img.loading = "lazy";
      img.referrerPolicy = "no-referrer";
      img.addEventListener("click", () => openLightbox(m.image, m.title));
      art.appendChild(img);
    }
    const pad = document.createElement("div");
    pad.className = "pad";
    const trad = m.tradition ? `<div class="trad">${m.tradition}</div>` : "";
    pad.innerHTML = `
      ${trad}
      <div class="kind">${m.kind || ""} ${m.date ? "· " + m.date : ""}</div>
      <h3>${m.title}</h3>
      ${compact ? "" : `<p class="prose">${m.significance || ""}</p>`}
      <div class="use">${m.debate_use || ""}</div>`;
    const links = [];
    if (m.viewer_url) links.push({ label: t("open_viewer", "Open viewer / source"), url: m.viewer_url });
    if (m.sources && !compact) links.push(...m.sources);
    pad.appendChild(receipts(links));
    art.appendChild(pad);
    return art;
  }

  function openLightbox(src, cap) {
    const box = $("lightbox");
    if (!box) return;
    $("lightbox-img").src = src;
    $("lightbox-cap").textContent = cap || "";
    box.hidden = false;
  }
  const lb = $("lightbox");
  if (lb) {
    lb.addEventListener("click", (e) => {
      if (e.target === lb || e.target.classList.contains("lightbox-close")) lb.hidden = true;
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") lb.hidden = true;
    });
  }

  function renderMaterials(filter) {
    const mats = $("materials");
    if (!mats) return;
    mats.innerHTML = "";
    (data.materials || [])
      .filter((m) => {
        if (!filter || filter === "all") return true;
        return (m.tradition || "") === filter;
      })
      .forEach((m) => mats.appendChild(materialCard(m, false)));
  }
  const matFilter = $("mat-filter");
  if (matFilter) matFilter.addEventListener("change", () => renderMaterials(matFilter.value));
  renderMaterials("all");

  // Debates
  const debatesEl = $("debates");
  if (debatesEl && data.debates) {
    data.debates.forEach((d, i) => {
      const details = document.createElement("details");
      details.className = "card";
      if (i === 0) details.open = true;
      const summary = document.createElement("summary");
      summary.innerHTML = `
        <div class="meta-line">
          <span>${d.year || ""}</span><span>${d.venue || ""}</span>
          <span>${(d.participants || []).join(" · ")}</span>
        </div>
        <h2>${d.title}</h2>`;
      const body = document.createElement("div");
      body.className = "body";
      if (d.motion) body.innerHTML += `<p class="prose"><strong>${t("motion", "Motion:")}</strong> ${d.motion}</p>`;
      body.innerHTML += `<p class="prose">${d.summary || ""}</p>`;
      if (d.key_moves) {
        const two = document.createElement("div");
        two.className = "two";
        Object.entries(d.key_moves).forEach(([side, moves]) => {
          const box = document.createElement("div");
          box.className = "note";
          box.innerHTML = `<strong>${side}</strong>`;
          const ul = document.createElement("ul");
          ul.className = "list-clean";
          (moves || []).forEach((mv) => {
            const li = document.createElement("li");
            li.textContent = mv;
            ul.appendChild(li);
          });
          box.appendChild(ul);
          two.appendChild(box);
        });
        body.appendChild(two);
      }
      if (d.timestamps && d.timestamps.length) {
        const box = document.createElement("div");
        box.className = "data-box";
        const lab = document.createElement("div");
        lab.className = "label";
        lab.textContent = t("timestamps", "Timestamps (prep)");
        box.appendChild(lab);
        const ul = document.createElement("ul");
        ul.className = "list-clean";
        const yt = youtubeWatchUrl(d.links);
        d.timestamps.forEach((row) => {
          const li = document.createElement("li");
          if (yt && row.t) {
            const a = document.createElement("a");
            a.href = yt + "&t=" + clockToSeconds(row.t) + "s";
            a.target = "_blank";
            a.rel = "noopener";
            a.textContent = row.t;
            li.appendChild(a);
            li.appendChild(document.createTextNode(" — " + (row.label || "")));
          } else {
            li.textContent = (row.t || "") + " — " + (row.label || "");
          }
          ul.appendChild(li);
        });
        box.appendChild(ul);
        body.appendChild(box);
      }
      if (d.what_to_steal) {
        const steal = document.createElement("div");
        steal.className = "use";
        steal.innerHTML = `<strong>${t("steal", "Steal:")}</strong> ${d.what_to_steal.join(" · ")}`;
        body.appendChild(steal);
      }
      body.appendChild(receipts(d.links || []));
      details.append(summary, body);
      debatesEl.appendChild(details);
    });
  }

  // Opponent cards
  const cardsEl = $("cards");
  if (cardsEl && data.opponent_cards) {
    data.opponent_cards.forEach((c) => {
      const el = document.createElement("article");
      el.className = "card-static";
      el.innerHTML = `
        <div class="trigger">${t("if_they_say_colon", "If they say:")}</div>
        <h3>“${c.trigger}”</h3>
        <p class="prose"><strong>${t("fast_answer", "Fast answer:")}</strong> ${c.fast_answer}</p>
        <p class="prose"><strong>${t("follow_up", "Follow-up:")}</strong> ${c.follow_up || ""}</p>`;
      if (c.sources) {
        const src = document.createElement("p");
        src.className = "note";
        src.style.marginTop = "0.5rem";
        src.textContent = t("anchor", "Anchor: ") + (Array.isArray(c.sources) ? c.sources.join(" · ") : c.sources);
        el.appendChild(src);
      }
      cardsEl.appendChild(el);
    });
  }

  // Bibliography
  const bib = $("bib");
  if (bib && data.bibliography) {
    data.bibliography.forEach((tier) => {
      const block = document.createElement("section");
      block.className = "card-static";
      block.innerHTML = `<h3>${tier.tier}</h3>`;
      block.appendChild(receipts(tier.items || []));
      bib.appendChild(block);
    });
  }

  // Checklist
  const check = $("checklist");
  if (check && data.checklist) {
    data.checklist.forEach((item, i) => {
      const li = document.createElement("li");
      li.textContent = `${i + 1}. ${item}`;
      check.appendChild(li);
    });
  }

  // Live desk
  const liveLines = $("live-lines");
  const liveQuotes = $("live-quotes");
  const liveMss = $("live-mss");
  if (liveLines) {
    (data.arguments || []).forEach((arg) => {
      const live = arg.live || arg.live_lines;
      if (!live || !live.if_they_say) return;
      const el = document.createElement("article");
      el.className = "card-static";
      el.innerHTML = `<div class="trigger">${t("if_they_say", "If they say")}</div><h3>“${live.if_they_say}”</h3>`;
      const box = document.createElement("dl");
      box.className = "live-box";
      [
        [t("you_say", "You say"), live.you_say],
        [t("dont_overclaim", "Do not overclaim"), live.dont_overclaim],
      ].forEach(([k, v]) => {
        if (!v) return;
        const dt = document.createElement("dt");
        dt.textContent = k;
        const dd = document.createElement("dd");
        dd.textContent = v;
        box.append(dt, dd);
      });
      el.appendChild(box);
      liveLines.appendChild(el);
    });
  }
  if (liveQuotes) {
    const seen = new Set();
    (data.arguments || []).forEach((arg) => {
      const quoteSides = [...new Set([...(data.meta.side_keys || []), "christian", "muslim", "israel", "palestine", "claimant", "critic"])];
      quoteSides.forEach((side) => {
        ((arg[side] && arg[side].quotes) || []).forEach((q) => {
          const key = (q.text || "") + (q.who || "");
          if (!q.text || seen.has(key)) return;
          seen.add(key);
          const wrap = quotesBlock([q]);
          if (wrap) liveQuotes.appendChild(wrap);
        });
      });
    });
  }
  if (liveMss) {
    (data.materials || [])
      .filter((m) => m.viewer_url)
      .forEach((m) => liveMss.appendChild(materialCard(m, true)));
  }

  // Global search
  function fold(s) {
    return String(s || "")
      .normalize("NFD")
      .replace(/\p{M}/gu, "")
      .toLowerCase();
  }
  function hay(obj) {
    return fold(JSON.stringify(obj));
  }
  const searchIndex = [];
  if (data.opening_speech) {
    searchIndex.push({
      kind: t("kind_speech", "Speech"),
      title: data.opening_speech.title || t("tab_speech", "Opening speech"),
      body: [data.opening_speech.lede, ...((data.opening_speech.paragraphs || []).map((p) => p.text))].filter(Boolean).join(" "),
      tab: "speech",
    });
  }
  (data.trinity_proofs || []).forEach((p) => {
    searchIndex.push({
      kind: t("kind_proof", "Their verse"),
      title: p.they_say || p.hook || "",
      body: [p.they_claim, p.counter, p.steelman, p.hook, p.pattern].filter(Boolean).join(" "),
      tab: "proofs",
    });
    (p.verses || []).forEach((v) => {
      searchIndex.push({
        kind: t("kind_verse", "Verse"),
        title: v.ref,
        body: v.hook || p.they_say || "",
        url: v.url,
        tab: "proofs",
      });
    });
  });
  (data.arguments || []).forEach((arg) => {
    const keys = data.meta.side_keys || ["christian", "muslim"];
    const a = arg[keys[0]] || arg.christian || {};
    const b = arg[keys[1]] || arg.muslim || {};
    searchIndex.push({
      kind: t("kind_argument", "Claim"),
      title: arg.title || arg.id || "",
      body: [arg.crux, arg.why_it_matters, a.claim, a.case, b.claim, b.case].filter(Boolean).join(" "),
      tab: "arguments",
    });
    const live = arg.live || arg.live_lines;
    if (live && live.if_they_say) {
      searchIndex.push({
        kind: t("kind_live", "Live line"),
        title: live.if_they_say,
        body: live.you_say || "",
        tab: "live",
      });
    }
    const quoteSides = [...new Set([...(data.meta.side_keys || []), "christian", "muslim", "israel", "palestine", "claimant", "critic"])];
    quoteSides.forEach((side) => {
      ((arg[side] && arg[side].quotes) || []).forEach((q) => {
        searchIndex.push({
          kind: t("kind_quote", "Quote"),
          title: (q.who || "") + " — " + (q.work || ""),
          body: [q.text, q.gloss, q.orig].filter(Boolean).join(" "),
          url: q.url,
          tab: "live",
        });
      });
    });
  });
  (data.opponent_cards || []).forEach((c) => {
    searchIndex.push({
      kind: t("kind_card", "Card"),
      title: c.trigger,
      body: c.fast_answer,
      tab: "cards",
    });
  });
  (data.materials || []).forEach((m) => {
    searchIndex.push({
      kind: t("kind_mss", "Manuscript"),
      title: m.title,
      body: (m.significance || "") + " " + (m.debate_use || ""),
      url: m.viewer_url,
      tab: "materials",
    });
  });
  (data.verse_catalog || []).forEach((g) => {
    searchIndex.push({
      kind: t("kind_verse_group", "Verse group"),
      title: g.title,
      body: [g.move || g.uthman, g.christian].filter(Boolean).join(" "),
      tab: "verses",
    });
    (g.verses || []).forEach((v) => {
      searchIndex.push({
        kind: t("kind_verse", "Verse"),
        title: v.ref,
        body: v.hook || "",
        url: v.url,
        tab: "verses",
      });
    });
  });

  const searchBox = $("live-search");
  const hitsEl = $("search-hits");
  if (searchBox && hitsEl) {
    searchBox.addEventListener("input", () => {
      const q = fold(searchBox.value.trim());
      hitsEl.innerHTML = "";
      if (q.length < 2) {
        hitsEl.hidden = true;
        return;
      }
      const hits = searchIndex.filter((row) => hay(row).includes(q)).slice(0, 12);
      hitsEl.hidden = !hits.length;
      hits.forEach((row) => {
        const div = document.createElement("div");
        div.className = "search-hit";
        div.innerHTML = `<div class="kind">${row.kind}</div><strong>${row.title}</strong><div>${row.body || ""}</div>`;
        if (row.url) {
          const a = document.createElement("a");
          a.href = row.url;
          a.target = "_blank";
          a.rel = "noopener";
          a.textContent = t("open", "Open");
          div.appendChild(a);
        }
        const go = document.createElement("button");
        go.type = "button";
        go.textContent = t("go_to", "Go to ") + row.tab;
        go.addEventListener("click", () => {
          const btn = document.querySelector(`[data-tab="${row.tab}"]`);
          if (btn) btn.click();
        });
        div.appendChild(go);
        hitsEl.appendChild(div);
      });
    });
  }
})();
