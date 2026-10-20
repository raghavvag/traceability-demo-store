"""Refund handling. Implements REQ-04 (Refund Transaction Integrity)."""

from fastapi import APIRouter, HTTPException

from app import ledger
from app.models import RefundReceipt, RefundRequest

router = APIRouter(prefix="/api/v1")


@router.post("/refund", response_model=RefundReceipt)
def process_refund(req: RefundRequest) -> RefundReceipt:
    """Refund a completed order. The server generates the refund reference."""
    order = ledger.get_order(req.order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    if req.refund_amount > order.total:
        raise HTTPException(status_code=422, detail="Refund exceeds the order total")
    refund_id, reference = ledger.record_refund(req.order_id, req.refund_amount, req.reason)
    return RefundReceipt(refund_id=refund_id, refund_reference=reference, order_id=req.order_id,
                         refund_amount=req.refund_amount, status="processed")
