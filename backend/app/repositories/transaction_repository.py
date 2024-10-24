from sqlalchemy.orm import Session
from app.models.Transaction import Transaction, TransactionType
from app.utils.error_handler import handle_db_exceptions


class TransactionRepository:
    """
    Repository for handling CRUD operations related to the 'Transaction' model.
    """

    @staticmethod
    @handle_db_exceptions
    def get_all_transactions(db: Session):
        """
        Retrieves all transactions from the database.

        :param db: Database session
        :return: List of all transactions
        """
        return db.query(Transaction).all()

    @staticmethod
    @handle_db_exceptions
    def create_transaction(db: Session, transaction: Transaction):
        """
        Creates a new transaction in the database.

        :param db: Database session
        :param transaction: Transaction object to create
        :return: Created transaction object
        """
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction

    @staticmethod
    @handle_db_exceptions
    def is_fund_already_subscribed(db: Session, fund_id: str) -> bool:
        """
        Checks if there is an active subscription to the given fund.

        :param db: Database session
        :param fund_id: ID of the fund
        :return: True if there is an active subscription, False otherwise
        """
        return (
            db.query(Transaction)
            .filter(
                Transaction.fund_id == fund_id,
                Transaction.type == TransactionType.SUBSCRIPTION,
            )
            .first()
            is not None
        )
