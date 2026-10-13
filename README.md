# Lexus Guardian AI

**AI-powered Churn Journey Prediction & Smart Intervention Engine**

Lexus Guardian AI is a prototype customer-retention decision system designed for Lexus after-sales teams.

It aims to answer:
1. Who may be at risk of leaving Lexus authorized service?
2. Why may they leave?
3. Which stage of the churn journey are they in?
4. What should Lexus do next?

> Prototype status: v0.1  
> Current scoring and journey classification are heuristic/rule-based for concept validation, not production-calibrated.

## Core Flow

`Listen -> Understand -> Predict -> Decide -> Act -> Learn`

## Churn Journey

`Stable -> Complaint -> Doubt -> Comparison -> Alternative Search -> Churn`

## Five Risk Dimensions

- Price Risk
- Trust Risk
- Service Risk
- Transparency Risk
- Alternative Risk

## Core Moat

**Persona × Journey × Intervention × Outcome**

The long-term value is not the LLM itself, but the Lexus-specific intervention knowledge accumulated from real outcomes.

## Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Run API:

```bash
python api/app.py
```

Then POST to:

```text
http://127.0.0.1:7000/analyze
```

## Repository Structure

```text
Lexus-Guardian-AI/
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ main.py
├─ data/
├─ src/
├─ api/
├─ prototype/
├─ docs/
├─ examples/
└─ tests/
```

## Current Prototype

- starter social-discussion dataset
- five-dimension churn risk scoring
- churn journey classification
- trigger detection
- Next Best Action rules
- Flask API
- documentation / architecture

## Future Development

- LLM-based automatic labeling
- persona clustering
- trigger graph learning
- Lexus service-knowledge RAG
- CRM / LINE / APP integration
- intervention outcome learning
- retention uplift estimation

## Data & Ethics

Sample records are anonymized and paraphrased for concept validation. The project does not attempt to identify real individuals.

**Lexus Guardian AI — 從「發現抱怨」進化到「預防流失」。**


## Web Prototype

Run:

```bash
python -m api.app
```

Then open:

```text
http://127.0.0.1:7000/
```

The prototype provides:
- customer post input
- persona selection
- five risk dimensions
- churn score
- journey stage
- primary trigger
- next best action


## Premium Web UI

v0.4 includes a redesigned competition/demo interface with:

- premium Lexus-inspired visual system
- churn journey visualization
- interactive risk sliders
- churn score panel
- AI interpretation
- primary trigger
- Next Best Action
- visual risk profile
