from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
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
