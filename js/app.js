(() => {
  const data = window.DEBATE_DATA;
  if (!data) return;

  const listEl = document.getElementById("list");
  const filterEl = document.getElementById("type-filter");
  const expandAllBtn = document.getElementById("expand-all");
  const collapseAllBtn = document.getElementById("collapse-all");
  const countEl = document.getElementById("count");

  document.getElementById("topic-title").textContent = data.topic.title;
  document.getElementById("thesis").textContent = data.topic.thesis;
  document.getElementById("scope").textContent = data.topic.scope;

  const methodList = document.getElementById("method-list");
  data.topic.method.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    methodList.appendChild(li);
  });

  const types = [...new Set(data.arguments.map((a) => a.type))].sort();
  types.forEach((type) => {
    const opt = document.createElement("option");
    opt.value = type;
    opt.textContent = type;
    filterEl.appendChild(opt);
  });

  function receiptList(receipts) {
    const ul = document.createElement("ul");
    ul.className = "receipts";
    receipts.forEach((r) => {
      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = r.url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = r.label;
      const note = document.createElement("span");
      note.className = "note";
      note.textContent = r.note;
      li.append(a, note);
      ul.appendChild(li);
    });
    return ul;
  }

  function sideBlock(kind, side) {
    const div = document.createElement("section");
    div.className = `side ${kind}`;
    const label = document.createElement("div");
    label.className = "label";
    label.textContent = kind === "christian" ? "Christian critique" : "Documented response";
    const claim = document.createElement("p");
    claim.className = "claim";
    claim.textContent = side.claim;
    const caseP = document.createElement("p");
    caseP.className = "case";
    caseP.textContent = side.case;
    div.append(label, claim, caseP, receiptList(side.receipts));
    return div;
  }

  function render(filterType) {
    listEl.innerHTML = "";
    const items = data.arguments.filter(
      (a) => !filterType || filterType === "all" || a.type === filterType
    );
    countEl.textContent = `${items.length} mapped`;

    items.forEach((arg, i) => {
      const details = document.createElement("details");
      details.className = "card";
      details.style.animationDelay = `${i * 40}ms`;
      details.dataset.type = arg.type;

      const summary = document.createElement("summary");
      const top = document.createElement("div");
      top.className = "summary-top";
      top.innerHTML = `<span class="num">#${arg.rank}</span><span>${arg.type}</span><span>${arg.popularity} in apologetics</span>`;
      const h2 = document.createElement("h2");
      h2.textContent = arg.title;
      const hint = document.createElement("div");
      hint.className = "summary-hint";
      hint.textContent = "Critique → response → receipts → crux";
      summary.append(top, h2, hint);

      const panel = document.createElement("div");
      panel.className = "panel";
      panel.append(sideBlock("christian", arg.christian), sideBlock("response", arg.response));

      const crux = document.createElement("section");
      crux.className = "crux";
      crux.innerHTML = `<div class="label">Crux</div>`;
      const cruxP = document.createElement("p");
      cruxP.textContent = arg.crux;
      crux.appendChild(cruxP);
      panel.appendChild(crux);

      details.append(summary, panel);
      listEl.appendChild(details);
    });
  }

  filterEl.addEventListener("change", () => render(filterEl.value));
  expandAllBtn.addEventListener("click", () => {
    listEl.querySelectorAll("details").forEach((d) => {
      d.open = true;
    });
  });
  collapseAllBtn.addEventListener("click", () => {
    listEl.querySelectorAll("details").forEach((d) => {
      d.open = false;
    });
  });

  render("all");
})();
