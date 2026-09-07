(() => {
  const data = window.DEBATE_DATA;
  if (!data) return;

  const $ = (id) => document.getElementById(id);
  const transcriptEl = $("transcript");
  const searchEl = $("search");
  const segments = data.transcript?.segments || [];

  $("title").textContent = data.meta?.title || "Ошибки Островского";
  $("subtitle").textContent = [data.meta?.debate, data.meta?.duration_fmt, data.meta?.error_count && `${data.meta.error_count} кандидатов`]
    .filter(Boolean)
    .join(" · ");

  $("status").textContent =
    "С телефона удобнее читать карточки и транскрипт. Таймкод — чтобы найти место в записи Instagram.";
  $("errors-intro").textContent =
    "Кандидаты для ролика. hard — текст против него прямой. likely — сильный ход. check — сначала сверь звук.";

  function showTab(id) {
    document.querySelectorAll("[data-tab]").forEach((b) => b.setAttribute("aria-selected", String(b.dataset.tab === id)));
    document.querySelectorAll("[data-panel]").forEach((p) => p.classList.toggle("hidden", p.dataset.panel !== id));
    if (location.hash.replace("#", "") !== id) history.replaceState(null, "", "#" + id);
  }

  document.querySelectorAll("[data-tab]").forEach((btn) => {
    btn.addEventListener("click", () => showTab(btn.dataset.tab));
  });
  const start = location.hash.replace("#", "");
  if (start && document.querySelector(`[data-tab="${start}"]`)) showTab(start);

  function jumpTranscript(sec) {
    showTab("transcript");
    let idx = 0;
    for (let i = segments.length - 1; i >= 0; i--) {
      if (sec >= segments[i].start - 0.05) {
        idx = i;
        break;
      }
    }
    renderTranscript(searchEl ? searchEl.value : "", idx);
    requestAnimationFrame(() => {
      const active = transcriptEl.querySelector(".seg.active");
      if (active) active.scrollIntoView({ block: "center" });
    });
  }

  function renderTranscript(filter, activeStart) {
    if (!transcriptEl) return;
    transcriptEl.innerHTML = "";
    const q = (filter || "").trim().toLowerCase();
    segments.forEach((seg) => {
      if (q && !seg.text.toLowerCase().includes(q)) return;
      const row = document.createElement("div");
      const isActive = activeStart != null && Math.abs(seg.start - activeStart) < 0.2;
      row.className = "seg" + (isActive ? " active" : "");
      row.innerHTML = `<div class="ts">${seg.start_fmt}</div><div>${seg.text}</div>`;
      row.addEventListener("click", () => {
        navigator.clipboard.writeText(`[${seg.start_fmt}] ${seg.text}`).catch(() => {});
      });
      transcriptEl.appendChild(row);
    });
  }

  function renderErrors(status) {
    const box = $("errors");
    box.innerHTML = "";
    (data.errors || [])
      .filter((e) => !status || status === "all" || e.status === status)
      .forEach((e) => {
        const art = document.createElement("article");
        art.className = "error";
        art.innerHTML = `
          <div class="bar">
            <span class="tag ${e.status}">${e.status}</span>
            <span class="tag ts">${e.start_fmt}</span>
            <span class="tag">#${e.n}</span>
          </div>
          <h3>${e.n}. ${e.title}</h3>
          <div class="label">Он сказал</div>
          <p class="said">${e.he_said}</p>
          <div class="label">В ролике</div>
          <p class="fix">${e.problem}</p>
          <p class="meta-line">На экране: ${e.on_screen || ""}</p>`;
        const refs = document.createElement("div");
        refs.className = "refs";
        (e.verses || []).forEach((v) => {
          const a = document.createElement("a");
          a.href = v.url;
          a.target = "_blank";
          a.rel = "noopener";
          a.textContent = v.ref;
          refs.appendChild(a);
        });
        (e.quran || []).forEach((v) => {
          const a = document.createElement("a");
          a.href = v.url;
          a.target = "_blank";
          a.rel = "noopener";
          a.textContent = "Коран " + v.ref;
          refs.appendChild(a);
        });
        if (e.kb) {
          const a = document.createElement("a");
          a.href = e.kb;
          a.textContent = "База";
          refs.appendChild(a);
        }
        const tools = document.createElement("div");
        tools.className = "toolbar";
        const toTs = document.createElement("button");
        toTs.type = "button";
        toTs.textContent = "К транскрипту " + e.start_fmt;
        toTs.addEventListener("click", () => jumpTranscript(e.start));
        const copy = document.createElement("button");
        copy.type = "button";
        copy.className = "secondary";
        copy.textContent = "Копировать";
        copy.addEventListener("click", () => {
          navigator.clipboard.writeText(`#${e.n} ${e.title}\n${e.start_fmt}\nОн: ${e.he_said}\nОтвет: ${e.problem}`);
        });
        tools.append(toTs, copy);
        art.append(refs, tools);
        box.appendChild(art);
      });
  }

  (data.chapters || []).forEach((ch) => {
    const li = document.createElement("li");
    li.innerHTML = `<div class="t">${ch.start_fmt}</div>${ch.title}`;
    li.addEventListener("click", () => jumpTranscript(ch.start));
    $("chapters").appendChild(li);
  });

  (data.video_shape || []).forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    $("shape").appendChild(li);
  });
  (data.checklist || []).forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    $("checklist").appendChild(li);
  });

  $("status-filter").addEventListener("change", (e) => renderErrors(e.target.value));
  if (searchEl) searchEl.addEventListener("input", () => renderTranscript(searchEl.value));
  $("copy-all").addEventListener("click", () => {
    const text = segments.map((s) => `[${s.start_fmt}] ${s.text}`).join("\n");
    navigator.clipboard.writeText(text);
  });

  renderErrors("all");
  renderTranscript("");
})();
