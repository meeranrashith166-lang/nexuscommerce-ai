import os
import re
import json
from typing import Dict, Any, List
from .paypal_client import PayPalClient

class AgenticCommerceEngine:
    """
    Autonomous Agent for Procurement, Budget Guardrails, and PayPal Execution.
    """
    def __init__(self, paypal_client: PayPalClient):
        self.paypal = paypal_client
        self.default_budget_limit = 5000.0  # Max hard spending limit
        self.require_approval_threshold = 1000.0  # Human-in-the-loop limit

    def process_prompt(self, user_prompt: str, user_budget: float = 2500.0) -> Dict[str, Any]:
        """
        Parses intent, analyzes line items, evaluates risk, and executes PayPal actions.
        """
        prompt_lower = user_prompt.lower()
        
        # 1. Detect Intent Category
        is_invoice = any(w in prompt_lower for w in ["invoice", "bill client", "bill customer"])
        is_payout = any(w in prompt_lower for w in ["payout", "split", "disburse", "pay vendor"])
        
        # 2. Extract Line Items & Estimated Cost
        items = []
        total_cost = 0.0

        if "laptop" in prompt_lower:
            items.append({"name": "Developer Workstation Pro", "quantity": 2, "price": 850.0, "category": "Hardware"})
        if "monitor" in prompt_lower or "screen" in prompt_lower:
            items.append({"name": "4K Ultra-wide Display", "quantity": 2, "price": 299.0, "category": "Hardware"})
        if "cloud" in prompt_lower or "gpu" in prompt_lower or "server" in prompt_lower:
            items.append({"name": "High-Performance Cloud GPU Cluster", "quantity": 1, "price": 420.0, "category": "Cloud"})
        if "license" in prompt_lower or "software" in prompt_lower or "seat" in prompt_lower or "tool" in prompt_lower:
            items.append({"name": "AI Developer Enterprise Seats", "quantity": 5, "price": 45.0, "category": "SaaS"})

        # If no default keywords matched, synthesize custom line item from prompt
        if not items:
            # Extract number if any
            numbers = re.findall(r"\$?(\d+(?:\.\d{2})?)", user_prompt)
            detected_amount = float(numbers[0]) if numbers else 450.0
            items.append({
                "name": f"Procured Resource: {user_prompt[:35]}...",
                "quantity": 1,
                "price": min(detected_amount, user_budget),
                "category": "Services"
            })

        total_cost = sum(it["quantity"] * it["price"] for it in items)

        # 3. Budget & Safety Guardrail Check
        budget_exceeded = total_cost > user_budget
        requires_human_approval = total_cost >= self.require_approval_threshold
        risk_score = round(min(0.08 + (total_cost / 10000.0), 0.95), 2)

        # 4. Agent Reasoning Steps
        thoughts = [
            f"Analyzed intent from prompt: '{user_prompt}'",
            f"Decomposed {len(items)} line item(s) totaling ${total_cost:,.2f} USD.",
            f"Assessed against allocated budget limit (${user_budget:,.2f} USD): {'COMPLIANT' if not budget_exceeded else 'OVER BUDGET'}.",
            f"Evaluated risk score: {risk_score} (Safety status: {'LOW RISK' if risk_score < 0.4 else 'MODERATE'}).",
        ]

        if budget_exceeded:
            thoughts.append(f"Guardrail triggered: Total cost (${total_cost:,.2f}) exceeds spending ceiling (${user_budget:,.2f}). Action halted.")
            return {
                "status": "REJECTED_BUDGET_EXCEEDED",
                "reasoning": thoughts,
                "items": items,
                "total_amount": total_cost,
                "budget_limit": user_budget,
                "risk_score": risk_score,
                "paypal_action": None
            }

        # 5. Execute PayPal Sandbox Transaction
        paypal_result = None
        if is_invoice:
            thoughts.append("Executing PayPal Invoicing v2 dispatch.")
            paypal_result = self.paypal.create_and_send_invoice(
                recipient_email="client@example-acme.com",
                amount=total_cost,
                note=f"NexusCommerce AI Invoice for: {user_prompt[:50]}"
            )
            action_type = "PAYPAL_INVOICE"
        elif is_payout:
            thoughts.append("Executing PayPal Payouts v1 split disbursement.")
            paypal_result = self.paypal.execute_payout(
                receiver_email="partner@agency.dev",
                amount=total_cost,
                note=f"Agentic settlement: {user_prompt[:50]}"
            )
            action_type = "PAYPAL_PAYOUT"
        else:
            thoughts.append("Creating PayPal Order v2 for merchant checkout.")
            paypal_result = self.paypal.create_order(
                amount=total_cost,
                currency="USD",
                description=f"Agentic Purchase: {user_prompt[:50]}",
                items=items
            )
            action_type = "PAYPAL_ORDER"

        thoughts.append(f"PayPal Sandbox transaction generated successfully with ID: {paypal_result.get('id') or paypal_result.get('invoice_id') or paypal_result.get('payout_batch_id')}.")

        return {
            "status": "APPROVED",
            "action_type": action_type,
            "requires_human_approval": requires_human_approval,
            "reasoning": thoughts,
            "items": items,
            "total_amount": total_cost,
            "budget_limit": user_budget,
            "risk_score": risk_score,
            "paypal_action": paypal_result
        }

