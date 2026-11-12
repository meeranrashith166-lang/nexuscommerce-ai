# NexusCommerce AI 🤖💳
### Autonomous Agentic Commerce, Budget Guardrails & PayPal Settlement Protocol

[![Open Source License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PayPal Developer Platform](https://img.shields.io/badge/PayPal-Orders%20v2%20%7C%20Invoicing%20%7C%20Payouts-003087?logo=paypal)](https://developer.paypal.com/)
[![AG Grid Powered](https://img.shields.io/badge/AG%20Grid-Interactive%20Ledger-e0234e)](https://www.ag-grid.com/)
[![Render Deploy](https://img.shields.io/badge/Render-Blueprint%20Ready-46E3B7?logo=render)](https://render.com)

---

## 💡 Overview & Problem Statement
As autonomous AI agents begin managing corporate procurement, software provisioning, and vendor contracting, existing financial rails lack **safety guardrails**, **multi-party settlement**, and **human-in-the-loop oversight**.

**NexusCommerce AI** is an end-to-end Agentic Commerce protocol that bridges natural language business goals directly into **PayPal Developer Platform APIs** (Orders v2, Invoicing v2, and Payouts) with:
* **Deterministic Financial Guardrails:** Real-time budget limit verification, risk scoring, and authorization ceilings.
* **Autonomous Decomposition:** Translates high-level natural language prompts into itemized merchant purchase orders.
* **Real-Time Audit Ledger (AG Grid):** Full interactive telemetry with quick filtering, sorting, risk telemetry badges, and one-click CSV audit export.
* **Cloud & SDK Ready (Render & APIMatic):** Native `render.yaml` infrastructure-as-code and OpenAPI 3.1 specification for rapid SDK generation.

---

## 🏆 Target Hackathon Prize Categories
1. **Grand Prize / Best Use of Agentic Commerce (\$5,000 / \$12,000):** Deep autonomous multi-agent purchasing logic connected to PayPal Orders v2 and Payouts.
2. **Best Use of PayPal + AI (\$5,000):** End-to-end flow from natural language intent to live PayPal sandbox settlement.
3. **Best Use of AG Grid (\$5,000 / \$2,000 / \$1,000):** Real-time transaction audit ledger with custom status renderers, risk scoring, and data export.
4. **Best Use of Render (Render Credits):** Zero-config cloud deployment using `render.yaml`.
5. **Best Use of APIMatic (\$1,000):** Standardized OpenAPI 3.1 schema for SDK generation across client languages.

---

## 🏗️ System Architecture

```
[ User Prompt / Mission ]
          │
          ▼
┌───────────────────────────────────────┐
│       NexusCommerce AI Engine         │
│  - Intent & Line-Item Decomposition   │
│  - Budget Spending Limit Check        │
│  - Risk Scoring & Guardrail Policy    │
└──────────────────┬────────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
┌─────────────────┐ ┌──────────────────────────┐
│  PayPal Sandbox │ │    AG Grid Audit Ledger  │
│  - Orders v2    │ │  - Real-Time Data Stream │
│  - Invoicing v2 │ │  - Quick Filter & Sort   │
│  - Payouts v1   │ │  - CSV Export & Auditing │
└─────────────────┘ └──────────────────────────┘
```

---

## 🚀 Quickstart & Setup Instructions (Judges / Reviewers)

### Prerequisites
* Python 3.10+
* (Optional) Free PayPal Developer Sandbox account from [developer.paypal.com](https://developer.paypal.com)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/nexuscommerce-ai.git
cd nexuscommerce-ai
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Environment Configuration (Optional)
The application includes an **instant-run mode** that functions immediately out of the box. To connect directly to your live PayPal sandbox app:
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Enter your sandbox credentials:
   ```env
   PAYPAL_CLIENT_ID=your_sandbox_client_id
   PAYPAL_CLIENT_SECRET=your_sandbox_client_secret
   PAYPAL_ENVIRONMENT=sandbox
   ```

### 4. Start the Application
```bash
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser to: **[http://localhost:8000](http://localhost:8000)**

---

## 🎬 3-Minute Video Demo Outline (YouTube Submission)

| Timestamp | Section | Key Talking Point |
| :--- | :--- | :--- |
| **0:00 – 0:35** | **The Hook & Problem** | Autonomous agents need financial rails; unconstrained agent spending causes risk and compliance nightmares. |
| **0:35 – 1:20** | **Live Agentic Procurement** | Input prompt: *"Procure 2 developer workstations and 5 AI licenses under $2,200"*. Watch agent decompose line items, enforce budget, and create a PayPal Order v2. |
| **1:20 – 1:55** | **PayPal Sandbox Settlement** | Demonstrate one-click sandbox capture, and invoice generation for customer billing. |
| **1:55 – 2:35** | **AG Grid Audit Ledger** | Demonstrate AG Grid real-time sorting, quick search filtering, risk evaluation badges, and CSV export. |
| **2:35 – 3:00** | **Render & APIMatic Architecture** | Highlight `render.yaml` 1-click cloud deployment and OpenAPI SDK generation. |

---

## 📄 Open Source License
Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for complete details.

