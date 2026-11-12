# NexusCommerce AI 🤖💳
### Autonomous Agentic Commerce, Budget Guardrails & PayPal Settlement Protocol

[![Open Source License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PayPal Developer Platform](https://img.shields.io/badge/PayPal-Orders%20v2%20%7C%20Invoicing%20%7C%20Payouts-003087?logo=paypal)](https://developer.paypal.com/)
[![AG Grid Powered](https://img.shields.io/badge/AG%20Grid-Interactive%20Ledger-e0234e)](https://www.ag-grid.com/)
[![Render Deploy](https://img.shields.io/badge/Render-Blueprint%20Ready-46E3B7?logo=render)](https://render.com)

---

## 💡 Overview & Problem Statement

As autonomous AI agents begin managing corporate procurement, software provisioning, and vendor contracting, existing financial rails lack **safety guardrails**, **multi-party settlement**, and **human-in-the-loop oversight**.

**NexusCommerce AI** is an end-to-end Agentic Commerce protocol that bridges natural language business goals directly into **PayPal Developer Platform APIs** (Orders v2, Invoicing v2, and Payouts v1) with:

* **Deterministic Financial Guardrails:** Real-time budget limit verification, risk scoring, and authorization ceilings before any transaction is executed.
* **Autonomous Intent Decomposition:** Translates high-level natural language prompts into itemized merchant purchase orders with unit pricing and quantities.
* **Real-Time Audit Ledger (AG Grid):** Full interactive telemetry with quick filtering, sorting, custom risk chips, and one-click CSV audit export.
* **Multi-Theme Professional Interface:** Production-ready dark and light themes with an integrated application dashboard.
* **Cloud & SDK Ready (Render & APIMatic):** Native `render.yaml` infrastructure-as-code and OpenAPI 3.1 specification for rapid SDK generation.

---

## 🏗️ System Architecture

```
[ User Natural Language Goal ]
              │
              ▼
┌───────────────────────────────────────────┐
│         NexusCommerce AI Engine           │
│  - Intent & Line-Item Decomposition       │
│  - Budget Spending Limit Check            │
│  - Risk Scoring & Safety Policy Engine    │
└─────────────────────┬─────────────────────┘
                      │
            ┌─────────┴─────────┐
    [Compliant]               [Over Budget]
            │                       │
            ▼                       ▼
┌───────────────────────┐ ┌───────────────────┐
│ PayPal Developer APIs │ │  Guardrail Block  │
│  - Orders v2 (Capture)│ │  (Halt & Alert)   │
│  - Invoicing v2 (Send)│ └───────────────────┘
│  - Payouts v1 (Split) │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────────────────────────┐
│         AG Grid Real-Time Ledger          │
│  - Live Transaction Stream & Status Badges│
│  - Multi-Column Sorting & Quick Search    │
│  - One-Click Audit CSV Export             │
└───────────────────────────────────────────┘
```

---

## 🚀 How to Run the Application

### Prerequisites
* **Python 3.10+** installed on your system.
* *(Optional)* A free PayPal Developer account at [developer.paypal.com](https://developer.paypal.com) if you want to connect live sandbox credentials. The app runs in fully functional simulation mode out of the box with zero setup.

---

### Option 1: One-Click Quick Launch (Windows)

Simply double-click the **`start.bat`** file in the project root directory.

This automatically starts the server at:
👉 **[http://localhost:8000](http://localhost:8000)**

---

### Option 2: Run via Terminal (Windows, macOS, Linux)

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/meeranrashith166-lang/nexuscommerce-ai.git
   cd nexuscommerce-ai
   ```

2. **Install Python Dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Start the Web Server:**
   ```bash
   python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Open in Browser:**
   Visit **[http://localhost:8000](http://localhost:8000)** in any modern web browser.

---

## 🎮 Interactive Walkthrough & Testing Guide

Once the dashboard is open at `http://localhost:8000`:

### 1. Run an Approved Procurement Mission
* Navigate to the **Agent Console** from the left sidebar.
* Click the preset: **"💻 Workstations + SaaS Licenses"** (or type your own instruction).
* Set the **Budget Ceiling Slider** to **$2,500**.
* Click **Execute Agentic Pipeline**.
* **Result:** The agent decomposes the order into itemized lines ($1,925 total), verifies budget compliance, assigns a low risk score, and generates a **PayPal Orders v2** transaction.
* Click **Capture Order in Sandbox** to finalize settlement.

### 2. Test the Safety Guardrail (Over-Budget Block)
* Keep the same prompt ($1,925 total).
* Drag the **Budget Ceiling Slider** down to **$1,000**.
* Click **Execute Agentic Pipeline**.
* **Result:** The safety engine halts execution immediately, flags the order with a red **"Blocked by Guardrail"** alert, and halts all payment calls to protect company funds.

### 3. Generate a Client Invoice
* Select the preset: **"📄 Client Invoice (PayPal v2)"**.
* Click **Execute Agentic Pipeline**.
* **Result:** The agent formats and drafts a formal PayPal Invoicing v2 transaction for customer billing.

### 4. Explore the AG Grid Audit Ledger
* Navigate to **Audit Ledger** in the sidebar.
* Type any keyword (e.g. `Hardware`, `COMPLETED`, or an amount) into the search bar for instant filtering.
* Click on column headers to sort by Amount, Risk Score, or Timestamp.
* Click **Export CSV** to download a complete spreadsheet audit log.

### 5. Switch Themes
* Click the **🌙 Dark / ☀️ Light** button in the top-right header to toggle between dark mode and light mode.

---

## ⚙️ Configuration & Environment Variables (Optional)

The application includes an **instant zero-config mode** so reviewers and judges can test immediately. 

To link your personal PayPal Developer Sandbox account:

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Populate your sandbox keys from [developer.paypal.com/dashboard](https://developer.paypal.com/dashboard/applications/sandbox):
   ```env
   PAYPAL_CLIENT_ID=your_sandbox_client_id_here
   PAYPAL_CLIENT_SECRET=your_sandbox_client_secret_here
   PAYPAL_ENVIRONMENT=sandbox
   PORT=8000
   ```

---

## 🔌 API Endpoints Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/status` | Returns system health, PayPal connection status, and active modules |
| `POST` | `/api/agent/procure` | Submits natural language mission with budget ceiling for agent evaluation |
| `GET` | `/api/ledger` | Returns real-time transaction audit array for AG Grid |
| `POST` | `/api/paypal/capture-order` | Settles authorized PayPal sandbox orders |

---

## 📄 Open Source License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for complete terms.
