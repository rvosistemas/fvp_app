from sqlalchemy.orm import Session
from app.models.Transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository


def get_all_transactions(db: Session):
    """
    Retrieves all transactions from the database.

    :param db: Database session
    :return: List of all transactions
    """
    return TransactionRepository.get_all_transactions(db)


def create_transaction(db: Session, transaction_data: dict):
    """
    Creates a new transaction in the database.

    :param db: Database session
    :param transaction_data: Data for the new transaction
    :return: Created transaction object
    """
    new_transaction = Transaction(**transaction_data)
    return TransactionRepository.create_transaction(db, new_transaction)
