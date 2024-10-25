from typing import List
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from ..services.subscription_service import SubscriptionService
from ..config.database import get_db
from ..schemas.transaction_schema import TransactionResponse

router = APIRouter()


@router.post("/funds/subscribe", response_model=dict)
def subscribe_to_fund(
    fund_id: str = Body(..., embed=True),
    amount: float = Body(..., embed=True),
    user_balance: float = Body(..., embed=True),
    db: Session = Depends(get_db),
):
    """
    Subscribe to a fund by providing the fund_id, amount to invest, and user_balance.
    """
    try:
        transaction = SubscriptionService.subscribe_to_fund(
            db, fund_id, amount, user_balance
        )
        return {
            "message": f"Successfully subscribed to fund {fund_id}",
            "transaction": transaction,
        }
    except HTTPException as e:
        error_message = f"Failed to subscribe to fund {fund_id}: {e.detail}"
        return {"error": error_message}


@router.post("/funds/cancel", response_model=dict)
def cancel_fund_subscription(
    fund_id: str = Body(..., embed=True), db: Session = Depends(get_db)
):
    """
    Cancel a subscription to a fund by providing the fund_id.

    Example:
    - **fund_id**: The ID of the fund to cancel the subscription to.
    """
    try:
        transaction = SubscriptionService.cancel_fund_subscription(db, fund_id)
        return {
            "message": f"Successfully canceled subscription to fund {fund_id}",
            "transaction": transaction,
        }
    except HTTPException as e:
        error_message = f"Failed to cancel subscription to fund {fund_id}: {e.detail}"
        return {"error": error_message}


@router.get("/transactions/active", response_model=List[TransactionResponse])
def get_active_subscriptions(db: Session = Depends(get_db)):
    """
    Get active fund subscriptions (transactions).
    """
    return SubscriptionService.get_active_subscriptions(db)
