from sqlalchemy.orm import Session
from app.models.Fund import Fund
from app.repositories.fund_repository import FundRepository


def get_funds(db: Session):
    """
    Retrieves all funds from the database.

    :param db: Database session
    :return: List of all funds
    """
    return FundRepository.get_all_funds(db)


def get_fund_by_id(db: Session, fund_id: str):
    """
    Retrieves a fund by its ID.

    :param db: Database session
    :param fund_id: ID of the fund to retrieve
    :return: Fund object or None if not found
    """
    return FundRepository.get_fund_by_id(db, fund_id)


def create_fund(db: Session, fund_data: dict):
    """
    Creates a new fund in the database.

    :param db: Database session
    :param fund_data: Data for the new fund
    :return: Created fund object
    """
    new_fund = Fund(**fund_data)
    return FundRepository.create_fund(db, new_fund)


def delete_fund(db: Session, fund_id: str):
    """
    Deletes a fund by its ID.

    :param db: Database session
    :param fund_id: ID of the fund to delete
    :return: None
    """
    return FundRepository.delete_fund(db, fund_id)


def deactivate_fund(db: Session, fund_id: str):
    """
    Deactivates a fund by its ID.

    :param db: Database session
    :param fund_id: ID of the fund to deactivate
    :return: Deactivated fund object
    """
    return FundRepository.deactivate_fund(db, fund_id)
