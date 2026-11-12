import os
import uuid
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from .paypal_client import PayPalClient
from .agent import AgenticCommerceEngine

load_dotenv()

app = FastAPI(
    title="NexusCommerce AI - Autonomous PayPal Agent API",
    description="Agentic Commerce Protocol connecting AI Agents with PayPal Orders v2, Invoicing, and AG Grid Ledger.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

paypal_client = PayPalClient()
agent_engine = AgenticCommerceEngine(paypal_client)

# In-memory transaction audit ledger (rendered in AG Grid)
transaction_ledger = [
    {
        "id": "TXN-9021",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "agent_goal": "Procure 2 developer laptops and 5 SaaS licenses for team onboarding",
        "category": "Hardware & SaaS",
        "amount": 1925.00,
        "currency": "USD",
        "status": "COMPLETED",
        "action_type": "PAYPAL_ORDER",
        "paypal_id": "ORDER-9182A4C",
        "risk_score": 0.27,
        "mode": "Sandbox"
    },
    {
        "id": "TXN-9020",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "agent_goal": "Automated monthly cloud GPU compute cluster renewal",
        "category": "Cloud Infrastructure",
        "amount": 420.00,
        "currency": "USD",
        "status": "COMPLETED",
        "action_type": "PAYPAL_ORDER",
        "paypal_id": "ORDER-7719B2E",
        "risk_score": 0.12,
        "mode": "Sandbox"
    },
    {
        "id": "TXN-9019",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "agent_goal": "Invoice enterprise customer Acme Corp for AI integration consultation",
        "category": "Consulting Services",
        "amount": 3500.00,
        "currency": "USD",
        "status": "SENT",
        "action_type": "PAYPAL_INVOICE",
        "paypal_id": "INV2-8820B1",
        "risk_score": 0.15,
        "mode": "Sandbox"
    }
]

# Request / Response Models
class AgentPromptRequest(BaseModel):
    prompt: str = Field(..., examples=["Procure 2 cloud servers and 4 enterprise licenses under $1200 budget"])
    budget_limit: Optional[float] = Field(2500.0, examples=[2500.0])

class CaptureOrderRequest(BaseModel):
    order_id: str

@app.get("/api/status")
def get_status():
    return {
        "status": "online",
        "paypal_connected": paypal_client.has_credentials(),
        "environment": os.getenv("PAYPAL_ENVIRONMENT", "sandbox"),
        "client_id_configured": bool(paypal_client.client_id and paypal_client.client_id != "your_paypal_sandbox_client_id_here"),
        "version": "1.0.0",
        "features": ["PayPal Orders v2", "Invoicing v2", "Payouts v1", "AG Grid Ledger", "Agent Guardrails"]
    }

@app.post("/api/agent/procure")
def agent_procure(req: AgentPromptRequest):
    """
    Submits an instruction to the autonomous Agentic Commerce Engine.
    """
    if not req.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    result = agent_engine.process_prompt(req.prompt, req.budget_limit)

    # Record in transaction ledger for AG Grid
    if result["status"] == "APPROVED" and result.get("paypal_action"):
        action = result["paypal_action"]
        paypal_id = action.get("id") or action.get("invoice_id") or action.get("payout_batch_id")
        
        txn_entry = {
            "id": f"TXN-{uuid.uuid4().hex[:4].upper()}",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "agent_goal": req.prompt,
            "category": result["items"][0]["category"] if result["items"] else "General",
            "amount": result["total_amount"],
            "currency": "USD",
            "status": "APPROVED" if result.get("requires_human_approval") else "COMPLETED",
            "action_type": result["action_type"],
            "paypal_id": paypal_id,
            "risk_score": result["risk_score"],
            "mode": action.get("mode", "sandbox")
        }
        transaction_ledger.insert(0, txn_entry)

    return result

@app.get("/api/ledger")
def get_ledger():
    """
    Returns live transaction audit entries for AG Grid Enterprise / Community.
    """
    return transaction_ledger

@app.post("/api/paypal/capture-order")
def capture_order(req: CaptureOrderRequest):
    res = paypal_client.capture_order(req.order_id)
    # Update status in ledger
    for txn in transaction_ledger:
        if txn.get("paypal_id") == req.order_id:
            txn["status"] = "COMPLETED"
            break
    return res

# Mount Static UI directory
static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)

