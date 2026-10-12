const $ = (id) => document.getElementById(id);

function val(id){ return Number($(id).value); }

function drawBars(risks){
  const labels = {
    price_risk:"Price",
    trust_risk:"Trust",
    service_risk:"Service",
    transparency_risk:"Transparency",
    alternative_risk:"Alternative"
  };
  $("bars").innerHTML = Object.entries(risks).map(([k,v]) => `
    <div class="bar-row">
      <div class="bar-label"><span>${labels[k]}</span><strong>${v}</strong></div>
      <div class="bar-track"><div class="bar-fill" style="width:${v}%"></div></div>
    </div>
  `).join("");
}

$("analyzeBtn").addEventListener("click", async () => {
  $("analyzeBtn").textContent = "Analyzing...";
  $("analyzeBtn").disabled = true;

  const payload = {
    text: $("text").value,
    persona: $("persona").value,
    price_risk: val("price_risk"),
    trust_risk: val("trust_risk"),
    service_risk: val("service_risk"),
    transparency_risk: val("transparency_risk"),
    alternative_risk: val("alternative_risk")
  };

  try {
    const res = await fetch("/analyze", {
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify(payload)
    });
    const data = await res.json();
    if(!res.ok) throw new Error(data.error || "Analyze failed");

    $("score").textContent = data.churn_score;
    $("riskLevel").textContent = data.risk_level;
    $("riskLevel").className = "risk-badge " + data.risk_level.toLowerCase();
    $("stage").textContent = data.journey_stage;
    $("trigger").textContent = data.primary_trigger;
    $("action").textContent = data.next_best_action;
    drawBars(data.risk_dimensions);
  } catch(err) {
    alert(err.message);
  } finally {
    $("analyzeBtn").textContent = "Analyze Customer Risk";
    $("analyzeBtn").disabled = false;
  }
});