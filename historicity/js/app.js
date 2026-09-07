(() => {
  const data = window.PREP_DATA;
  if (!data) return;

  const $ = (id) => document.getElementById(id);

  $("thesis").textContent = data.meta.thesis;
  $("purpose").textContent = data.meta.purpose;
  $("warning").textContent = data.meta.warning;
  $("title").textContent = data.meta.title;

  // Tabs
  const tabs = document.querySelectorAll("[data-tab]");
  const panels = document.querySelectorAll("[data-panel]");
  tabs.forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.tab;
      tabs.forEach((b) => b.setAttribute("aria-selected", String(b === btn)));
      panels.forEach((p) => p.classList.toggle("active", p.dataset.panel === id));
      history.replaceState(null, "", "#" + id);
    });
  });
  const initial = location.hash.replace("#", "") || "brief";
  const start = document.querySelector(`[data-tab="${initial}"]`) || tabs[0];
  start.click();

  function receipts(items) {
    const ul = document.createElement("ul");
    ul.className = "receipts";
    (items || []).forEach((r) => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = r.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = r.label;
      li.appendChild(a);
      ul.appendChild(li);
    });
    return ul;
  }

  // Definitions
  const defs = $("defs");
  data.definitions.forEach((d) => {
    const el = document.createElement("article");
    el.className = "def";
    el.innerHTML = `<h3>${d.term}</h3><p class="prose">${d.precise}</p><p class="not">${d.not}</p>`;
    defs.appendChild(el);
  });

  // Positive cases
  const pillars = $("pillars");
  const cases = [
    ["If defending Bible historicity", data.positive_cases.if_defending_bible_historicity],
    ["If defending Qur'an historicity", data.positive_cases.if_defending_quran_historicity],
    ["If seeking unity / steelman", data.positive_cases.if_seeking_unity_steelman],
  ];
  cases.forEach(([title, items]) => {
    const card = document.createElement("article");
    card.className = "card-static";
    card.innerHTML = `<h3>${title}</h3>`;
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

  // Checklist
  const check = $("checklist");
  data.prep_checklist.forEach((item, i) => {
    const li = document.createElement("li");
    li.textContent = `${i + 1}. ${item}`;
    check.appendChild(li);
  });

  // Debates
  const debatesEl = $("debates");
  data.debates.forEach((d, i) => {
    const details = document.createElement("details");
    details.className = "card";
    if (i === 0) details.open = true;
    const summary = document.createElement("summary");
    summary.innerHTML = `
      <div class="meta-line">
        <span>${d.year}</span><span>${d.venue}</span>
        <span>${d.participants.join(" vs ")}</span>
      </div>
      <h2>${d.title}</h2>`;
    const body = document.createElement("div");
    body.className = "body";
    body.innerHTML = `
      <p class="prose"><strong>Motion:</strong> ${d.motion}</p>
      <p class="prose">${d.summary}</p>`;

    const two = document.createElement("div");
    two.className = "two";
    Object.entries(d.key_moves).forEach(([side, moves]) => {
      const box = document.createElement("div");
      box.className = "note";
      box.innerHTML = `<strong>${side}</strong>`;
      const ul = document.createElement("ul");
      ul.className = "list-clean";
      moves.forEach((m) => {
        const li = document.createElement("li");
        li.textContent = m;
        ul.appendChild(li);
      });
      box.appendChild(ul);
      two.appendChild(box);
    });
    body.appendChild(two);

    const steal = document.createElement("div");
    steal.className = "use";
    steal.innerHTML = `<strong>Steal for your prep:</strong>`;
    const sul = document.createElement("ul");
    sul.className = "list-clean";
    d.what_to_steal.forEach((s) => {
      const li = document.createElement("li");
      li.textContent = s;
      sul.appendChild(li);
    });
    steal.appendChild(sul);
    body.appendChild(steal);
    body.appendChild(receipts(d.links));

    details.append(summary, body);
    debatesEl.appendChild(details);
  });

  // Arguments
  const filter = $("arg-filter");
  const clusters = [...new Set(data.arguments.map((a) => a.cluster))];
  clusters.forEach((c) => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    filter.appendChild(opt);
  });

  const argsEl = $("arguments");
  function renderArgs(cluster) {
    argsEl.innerHTML = "";
    data.arguments
      .filter((a) => !cluster || cluster === "all" || a.cluster === cluster)
      .forEach((arg) => {
        const details = document.createElement("details");
        details.className = "card";
        const summary = document.createElement("summary");
        summary.innerHTML = `
          <div class="meta-line">
            <span>#${arg.rank}</span><span>${arg.cluster}</span>
            <span>${arg.type}</span><span>${arg.popularity}</span>
          </div>
          <h2>${arg.title}</h2>`;
        const body = document.createElement("div");
        body.className = "body";

        const two = document.createElement("div");
        two.className = "two";

        const bible = document.createElement("section");
        bible.className = "side bible";
        bible.innerHTML = `<div class="label">Bible-historicity case</div>
          <p class="claim">${arg.bible_case.claim}</p>
          <p class="case">${arg.bible_case.case}</p>`;
        bible.appendChild(receipts(arg.bible_case.sources));

        const quran = document.createElement("section");
        quran.className = "side quran";
        quran.innerHTML = `<div class="label">Qur'an-historicity case</div>
          <p class="claim">${arg.quran_case.claim}</p>
          <p class="case">${arg.quran_case.case}</p>`;
        quran.appendChild(receipts(arg.quran_case.sources));

        two.append(bible, quran);
        body.appendChild(two);

        const counters = document.createElement("div");
        counters.className = "two";
        counters.innerHTML = `
          <div class="note"><strong>Counter to Bible case:</strong> ${arg.counter_to_bible}</div>
          <div class="note"><strong>Counter to Qur'an case:</strong> ${arg.counter_to_quran}</div>`;
        body.appendChild(counters);

        const crux = document.createElement("div");
        crux.className = "crux";
        crux.textContent = "Crux: " + arg.crux;
        body.appendChild(crux);

        const use = document.createElement("div");
        use.className = "use";
        use.textContent = "Debate use: " + arg.debate_use;
        body.appendChild(use);

        details.append(summary, body);
        argsEl.appendChild(details);
      });
  }
  filter.addEventListener("change", () => renderArgs(filter.value));
  $("expand-args").addEventListener("click", () => {
    argsEl.querySelectorAll("details").forEach((d) => (d.open = true));
  });
  $("collapse-args").addEventListener("click", () => {
    argsEl.querySelectorAll("details").forEach((d) => (d.open = false));
  });
  renderArgs("all");

  // Opponent cards
  const cardsEl = $("cards");
  data.opponent_cards.forEach((c) => {
    const el = document.createElement("article");
    el.className = "card-static";
    el.innerHTML = `
      <div class="trigger">If they say:</div>
      <h3>“${c.trigger}”</h3>
      <p class="prose"><strong>Fast answer:</strong> ${c.fast_answer}</p>
      <p class="prose"><strong>Follow-up:</strong> ${c.follow_up}</p>`;
    const src = document.createElement("p");
    src.className = "note";
    src.style.marginTop = "0.55rem";
    src.textContent = "Anchor: " + c.sources.join(" · ");
    el.appendChild(src);
    cardsEl.appendChild(el);
  });

  // Bibliography
  const bib = $("bib");
  data.bibliography.forEach((tier) => {
    const block = document.createElement("section");
    block.className = "card-static";
    block.innerHTML = `<h3>${tier.tier}</h3>`;
    block.appendChild(receipts(tier.items));
    bib.appendChild(block);
  });
})();
