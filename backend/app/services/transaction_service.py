import datetime
from sqlalchemy.orm import Session
from ..models.Transaction import Transaction
from ..repositories.transaction_repository import TransactionRepository
from ..repositories.fund_repository import FundRepository


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
    fund = FundRepository.get_fund_by_id(db, transaction_data["fund_id"])
    transaction_code = generate_transaction_code(fund)
    new_transaction = Transaction(**transaction_data, code=transaction_code)
    return TransactionRepository.create_transaction(db, new_transaction)


def generate_transaction_code(fund):
    """
    Generates a unique transaction code based on the fund, ID and date.

    :param fund: Fund object
    :return: Generated transaction code
    """
    fund_initials = "".join([word[0].upper() for word in fund.name.split()])
    date_str = datetime.now().strftime("%Y%m%d")
    transaction_code = f"{fund_initials}{date_str}"
    return transaction_code
