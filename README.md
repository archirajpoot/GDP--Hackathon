# ⚖️ FairForge Arena

<div align="center">
  <img src="https://img.shields.io/badge/Google-Solution_Challenge_2026-blue?style=for-the-badge&logo=google" alt="Solution Challenge">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" alt="GCP">
  <img src="https://img.shields.io/badge/Gemini_AI-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white" alt="Gemini">
</div>

<br>

**Team:**  MASSIVE-X  
**Focus:** AI Fairness
**Track:** Unbiased AI Decision 

**FairForge Arena** is an accessible, enterprise-grade AI Fairness Training Gym . It is engineered to thoroughly inspect data sets and software models for hidden unfairness. By combining high-performance backend pipelines with Reinforcement Learning, FairForge provides organizations with an easy way to **measure, flag, and fix** harmful bias in automated decisions (finance, healthcare, hiring) *before* their systems impact real people.

---

## 🌍 UN Sustainable Development Goals (SDGs)
* **SDG 10 (Reduced Inequalities):** Prevents algorithmic discrimination against marginalized groups in life-changing automated decisions.
* **SDG 16 (Peace, Justice, and Strong Institutions):** Enforces transparency and institutional accountability via automated, accessible compliance reporting.

---

## ✨ Key Features

- **Interactive Intersectional Bias Heatmap** — Visualizes bias across gender, race, and age combinations.
- **PPO Training Arena** — Watch the AI agent learn to become fairer over episodes (real-time training curve).
- **Gemini Counterfactual Explainer** — Answers questions like *"Why was this applicant rejected?"* in plain English.
- **One-Click Mitigation Controls** — Apply fixes and instantly see the impact.
- **EU AI Act Compliance Reports** — Ready-to-submit governance documentation.
- **Real-Time Monitoring Simulation** — Demonstrates production-ready bias drift detection.

---

## 🚀 Core Capabilities: Measure, Flag, & Fix

1. **MEASURE: Automated Bias Detection:** Thoroughly inspects data sets to calculate Disparate Impact, Demographic Parity, and Equal Opportunity across intersectional vectors.
2. **FLAG: Live Bias Drift Monitoring:** WebSockets and REST endpoints simulate real-time MLOps monitoring, triggering automated alerts when fairness drops in production.
3. **FIX: Reinforcement Learning Mitigation:** An active "gym" (PPO) that trains biased models against adversarial edge-cases to mathematically optimize fairness.
4. **FIX: Gemini-Powered Counterfactuals:** Ingests complex fairness metrics and uses the Gemini API to output plain-English "What-If" scenarios to correct bias (e.g., *"If the applicant was 5 years older, approval probability increases by 12%"*).
5. **ACCESSIBILITY: Audit-Ready Reporting:** Generates downloadable, one-click PDF compliance reports hosted on Google Cloud Storage for non-technical stakeholders.

---

## 🏗️ Cloud & Backend Architecture

Built for scale, relying heavily on modern Data Cloud Engineering principles to ensure smooth integration into existing enterprise workflows:

* **Backend API:** `FastAPI` (Python) for high-concurrency, asynchronous ML routing.
* **AI Engine:** `PyTorch` (PPO training loop) Custom fairness_metrics + 12 policy rules & `Scikit-learn`.
* **LLM Layer:** Google Gemini API (Vertex AI) for natural language report generation.
* **RL Gym:**  OpenEnv + Stable-Baselines3 PPO Trainer.
* **Infrastructure (GCP):**
  * **Google Cloud Run:** Serverless, auto-scaling container deployment.
  * **Google Cloud Storage (GCS):** Secure blob storage for exported PDF audits.
  * **Firebase Auth:** JWT-based secure access for API endpoints.
  * **Docker:** Immutable, containerized environments for the entire MLOps pipeline.

---

## 📂 System Map

```text
fairforge/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI entry point & MLOps routes
│   ├── policies.py          # 12 fairness constraints & policies
│   ├── grader.py            # 6-metric fairness evaluation engine
│   ├── adversary.py         # Bias injector for stress-testing
│   ├── fairness_metrics.py  # Core mathematical logic to MEASURE bias
│   ├── mitigation_engine.py # Automated reweighting & FIX suggestions
│   └── gemini_auditor.py    # Google Gemini API integration for explanations
├── data/
│   └── tasks/               # Benchmark datasets (Hiring, Loans, Medical)
├── openenv/                 
│   ├── env.py               # RL environment for fairness simulation
│   ├── ppo_trainer.py       # PPO loop for algorithmic optimization
│   └── basilisk.py          # Core evaluation/grading scripts
├── reports/                 # Output directory for accessible compliance PDFs
├── Dockerfile               # Production container configuration
└── requirements.txt         # Dependency manifest


┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              USER JOURNEY (Top Layer)                               │
│                                                                                     │
│   ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐                │
│   │  UPLOAD  │ ───▶ │  AUDIT   │ ───▶ │ MITIGATE │ ───▶ │  EXPORT  │              │
│   │  Model/  │      │ Fairness │      │   Fix    │      │  Report  │                │
│   │  Data    │      │  Check   │      │  Bias    │      │  (PDF)   │                │
│   └────┬─────┘      └────┬─────┘      └────┬─────┘      └────┬─────┘                │
│        │                 │                 │                 │                      │
│        ▼                 ▼                 ▼                 ▼                      │
│   • Auto‑detect      • 7 Metrics       • One‑Click       • EU AI Act                │
│     schema           • Intersectional    (Reweight,       • Audit Logs              │
│   • Protected          Heatmap           Drop Proxy,      • Dataset                 │
│     attributes       • Violations        Threshold)         Export                  │
│                        Panel            • PPO RL                                    │
│                                          Training                                   │
│                                                                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│                    UNDER‑THE‑HOOD ARCHITECTURE (Bottom Layer)                       │
│                                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                           FRONTEND (User Interface)                         │   │
│   │                    Tailwind CSS  │  Plotly.js  │  Glassmorphism             │   |
│   └───────────────────────────────────────┬─────────────────────────────────────┘   │
│                                           │                                         │
│                                           ▼                                         │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                            BACKEND (FastAPI)                                │   │
│   │          PyTorch  │  Scikit‑learn  │  Fairness Metrics Engine               │   │
│   └───────┬───────────────────────────────┬───────────────────────────────┬─────┘   │
│           │                               │                               │         │
│           ▼                               ▼                               ▼         │
│   ┌───────────────────┐       ┌───────────────────┐       ┌───────────────────┐     │
│   │   RL ENGINE       │       │   XAI ENGINE      │       │   COMPLIANCE      │     │
│   │                   │       │                   │       │                   │     │
│   │ • Stable‑         │       │ • Gemini API      │       │ • Report          │     │
│   │   Baselines3 PPO  │       │ • Vertex AI       │       │   Generator       │     │
│   │ • Gymnasium Env   │       │ • Counterfactual  │       │ • Audit Trail     │     │
│   │                   │       │   What‑If         │       │   (Hash Chain)    │     │
│   │ Reward Function:  │       │ • Plain‑English   │       │                   │     │
│   │ α·Acc − β·|DI−1|  │       │   Explanations    │       │                   │     │
│   │      − γ·SPD      │       │                   │       │                   │     │
│   └───────────────────┘       └───────────────────┘       └───────────────────┘     │
│                                                                                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│                          📊 RESULTS & IMPACT                                       │
│                                                                                      │
│   Disparate Impact:  0.54 ───────────────────────────────▶ 0.89  (+65%) ✅          │
│   Statistical Parity: 0.23 ───────────────────────────────▶ 0.04  (−83%) ✅         │
│   Accuracy Trade‑off: 87% ────────────────────────────────▶ 84%   (−3%)             │
│                                                                                      │
│    ⏱️ Full workflow (upload → report): ~5 minutes (excluding training time)         │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘




        🧑‍💻 Data Scientist        📋 Compliance Officer        💼 Business Stakeholder

                        ┌────────────────────────────────────────┐
                        │         FAIRFORGE ARENA                │
                        │                                        │
                        │  🔍 DATA & MODEL AUDIT                 │
                        │  • Upload Dataset / Model              │
                        │  • Auto-Detect Attributes              │
                        │  • Detect Proxy Variables              │
                        │  • Compute Fairness Metrics            │
                        │  • Intersectional Analysis             │
                        │                                        │
                        │  🚩 MONITORING & FLAGGING              │
                        │  • Flag High-Risk Bias                 │
                        │  • Generate Bias Alerts                │
                        │  • Stress Testing (Edge Cases)         │
                        │  • Continuous Monitoring               │
                        │                                        │
                        │  🔧 MITIGATION (RL-BASED)              │
                        │  • Apply Bias Fixes                    │
                        │  • RL Training (PPO)                   │
                        │  • Threshold Optimization              │
                        │  • Compare Model Versions              │
                        │                                        │
                        │  🧠 EXPLAINABILITY (XAI)               │
                        │  • Gemini Chat Assistant               │
                        │  • Counterfactual Analysis             │
                        │  • Explain Decisions (Plain English)   │
                        │                                        │
                        │  📄 COMPLIANCE & REPORTING             │
                        │  • EU AI Act Reports                   │
                        │  • Audit Trail & Logs                  │
                        │  • Risk Documentation                  │
                        │  • Export Reports (PDF)                │
                        │                                        │
                        └────────────────────────────────────────┘

                                   ⚙️ System (Automated Engine)

                                   🚀FUTURE TO BUILD PRODUCT ROADMAP — FAIRFORGE ARENA

┌────────────────────────┬────────────────────────┬────────────────────────┬────────────────────────┐
│  PHASE 1 (0–3 Months)  │  PHASE 2 (3–6 Months)  │  PHASE 3 (6–12 Months) │  PHASE 4 (12+ Months)  │
│  FOUNDATION (v3.1)     │  SCALE (v4.0)          │  ENTERPRISE (v5.0)     │  GLOBAL PLATFORM       │
├────────────────────────┼────────────────────────┼────────────────────────┼────────────────────────┤
│ 🔧 Platform Stability  │ ⚡ Real-Time Systems  │ 🏢 Enterprise Features │ 🌍 Ecosystem Expansion│
│ • Production APIs      │ • Drift Monitoring     │ • SSO & RBAC           │ • Public Leaderboard   │
│ • RL Training Engine   │ • Live Bias Alerts     │ • Team Collaboration   │ • Regulatory Mapping   │
│ • Data Pipelines       │ • Continuous Auditing  │ • Audit Automation     │ • Global Compliance    │
│                        │                        │                        │                        │
│ 🧠 AI Enhancements     │ 🧪 Advanced AI         │ 🔐 Security & Privacy │🤝 Community & Research│
│ • Gemini Integration   │ • Causal AI Models     │ • Federated Auditing   │ • Open Source Ecosystem│
│ • XAI Improvements     │ • Shadow AI Detection  │ • Data Privacy Layers  │ • Research Papers      │
│ • Metric Expansion     │ • Multimodal Fairness  │ • Secure Logging       │ • Industry Partnerships│
│                        │                        │                        │                        │
│ 📊 Data & Models       │ 📊 Model Intelligence │ 📊 Governance          │ 💼 Business Growth    │
│ • Multi-Dataset        │ • Model Benchmarking   │ • Compliance Engine    │ • SaaS Platform        │
│ • Structured Data      │ • Model Comparison     │ • Policy Mapping       │ • Enterprise Clients   │
│ • Initial Support      │ • Version Tracking     │ • Risk Scoring         │ • Monetization         │
└────────────────────────┴────────────────────────┴────────────────────────┴────────────────────────┘