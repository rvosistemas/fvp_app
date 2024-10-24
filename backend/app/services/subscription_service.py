from datetime import datetime
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.Transaction import Transaction, TransactionType
from app.repositories.fund_repository import FundRepository
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction_schema import TransactionResponse


class SubscriptionService:

    @staticmethod
    def subscribe_to_fund(
        db: Session, fund_id: int, amount: float, user_balance: float
    ) -> TransactionResponse:
        """
        Subscribes to a fund if not already subscribed.
        """
        if TransactionRepository.is_fund_already_subscribed(db, fund_id):
            raise HTTPException(
                status_code=400, detail="You are already subscribed to this fund."
            )

        fund = FundRepository.get_fund_by_id(db, fund_id)

        if amount < fund.minimum_amount:
            raise HTTPException(
                status_code=400,
                detail=f"The amount must be at least {fund.minimum_amount} to subscribe to {fund.name}",
            )

        if user_balance < amount:
            raise HTTPException(
                status_code=400, detail="Insufficient balance for this subscription"
            )

        transaction = Transaction(
            fund_id=fund.id,
            type=TransactionType.SUBSCRIPTION,
            amount=amount,
            code=Transaction.generate_code(fund.id, fund.name),
        )
        TransactionRepository.create_transaction(db, transaction)

        return TransactionResponse.from_orm(transaction)

    @staticmethod
    def get_active_subscriptions(db: Session) -> List[TransactionResponse]:
        """
        Get all active subscriptions (transactions) and convert to Pydantic model.
        """
        transactions = TransactionRepository.get_active_transactions(db)

        return [
            TransactionResponse.from_orm(transaction) for transaction in transactions
        ]

    @staticmethod
    def cancel_fund_subscription(db: Session, fund_id: int):
        """
        Cancels a fund subscription by marking the transaction as inactive.
        """
        transaction = TransactionRepository.get_active_subscription(db, fund_id)

        if not transaction:
            raise HTTPException(
                status_code=404, detail="No active subscription found for this fund"
            )

        transaction.is_active = False
        db.commit()
        return TransactionResponse.from_orm(transaction)
