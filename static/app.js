const $ = (id) => document.getElementById(id);

const riskIds = [
  "price_risk",
  "trust_risk",
  "service_risk",
  "transparency_risk",
  "alternative_risk"
];

const labels = {
  price_risk: "Price",
  trust_risk: "Trust",
  service_risk: "Service",
  transparency_risk: "Transparency",
  alternative_risk: "Alternative"
};

riskIds.forEach(id => {
  const input = $(id);
  const value = $(`${id}_value`);
  input.addEventListener("input", () => value.textContent = input.value);
});

$("demoBtn").addEventListener("click", () => {
  $("text").value = "最近回原廠又叫我換一堆東西，報價快三萬，有人推薦台北 Lexus 外廠嗎？";
  $("persona").value = "價格敏感型";

  const demo = {
    price_risk: 88,
    trust_risk: 76,
    service_risk: 55,
    transparency_risk: 84,
    alternative_risk: 96
  };

  Object.entries(demo).forEach(([id, value]) => {
    $(id).value = value;
    $(`${id}_value`).textContent = value;
  });
});

function riskInterpretation(data){
  if (data.risk_level === "High") {
    return "此車主已出現明顯流失訊號，建議由售後團隊優先介入，避免進一步轉向外部保修體系。";
  }
  if (data.risk_level === "Medium") {
    return "此車主具有部分流失風險，建議持續觀察並針對主要風險原因提供個人化溝通。";
  }
  return "目前流失風險較低，可維持一般關係經營並持續監測後續訊號。";
}

function drawBars(risks){
  $("bars").innerHTML = Object.entries(risks).map(([k,v]) => `
    <div class="bar-row">
      <div class="bar-label">
        <span>${labels[k]}</span>
        <strong>${Math.round(v)}</strong>
      </div>
      <div class="bar-track">
        <div class="bar-fill" style="width:${Math.max(0, Math.min(100, v))}%"></div>
      </div>
    </div>
  `).join("");
}

$("analyzeBtn").addEventListener("click", async () => {
  const btn = $("analyzeBtn");
  btn.disabled = true;
  btn.innerHTML = "<span>Analyzing...</span><span class='arrow'>···</span>";

  const payload = {
    text: $("text").value.trim(),
    persona: $("persona").value,
    price_risk: Number($("price_risk").value),
    trust_risk: Number($("trust_risk").value),
    service_risk: Number($("service_risk").value),
    transparency_risk: Number($("transparency_risk").value),
    alternative_risk: Number($("alternative_risk").value)
  };

  if (!payload.text) {
    alert("請先輸入車主討論文字");
    btn.disabled = false;
    btn.innerHTML = "<span>Analyze Customer Risk</span><span class='arrow'>→</span>";
    return;
  }

  try {
    const res = await fetch("/analyze", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || "Analyze failed");

    $("score").textContent = Number(data.churn_score).toFixed(1);
    $("riskLevel").textContent = data.risk_level;
    $("riskLevel").className = `risk-pill ${data.risk_level.toLowerCase()}`;
    $("stage").textContent = data.journey_stage;
    $("trigger").textContent = data.primary_trigger;
    $("action").textContent = data.next_best_action;
    $("interpretation").textContent = riskInterpretation(data);

    drawBars(data.risk_dimensions);
  } catch (err) {
    alert(`分析失敗：${err.message}`);
  } finally {
    btn.disabled = false;
    btn.innerHTML = "<span>Analyze Customer Risk</span><span class='arrow'>→</span>";
  }
});