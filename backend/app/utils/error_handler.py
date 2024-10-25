from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models.Fund import Fund


def handle_db_exceptions(func):
    """
    Decorator to handle database exceptions and rollback transactions in case of an error.

    :param func: Function to be decorated
    :return: Wrapped function with error handling
    """

    def wrapper(*args, **kwargs):
        db = kwargs.get("db") or (args[0] if args else None)
        if db is None:
            raise ValueError("Database session must be provided as 'db' argument")

        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            if db:
                db.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    return wrapper


def get_fund_or_404(db: Session, fund_id: str):
    """
    Retrieves a fund by its ID or raises a 404 HTTPException if not found.

    :param db: Database session
    :param fund_id: ID of the fund to retrieve
    :return: Fund object or raises HTTPException if not found
    """
    fund = db.query(Fund).filter(Fund.id == fund_id).first()
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")
    return fund
