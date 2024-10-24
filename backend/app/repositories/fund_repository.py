from http.client import HTTPException
from sqlalchemy.orm import Session
from app.models.Fund import Fund
from app.utils.error_handler import handle_db_exceptions, get_fund_or_404


class FundRepository:
    """
    Repository for handling CRUD operations related to the 'Fund' model.
    """

    @staticmethod
    @handle_db_exceptions
    def get_all_funds(db: Session):
        """
        Retrieves all funds from the database.

        :param db: Database session
        :return: List of all funds
        """
        return db.query(Fund).all()

    @staticmethod
    @handle_db_exceptions
    def get_fund_by_id(db: Session, fund_id: str):
        """
        Retrieves a fund by its ID.

        :param db: Database session
        :param fund_id: ID of the fund to retrieve
        :return: Fund object or None if not found
        :raises HTTPException: If fund is not found
        """
        return get_fund_or_404(db, fund_id)

    @staticmethod
    @handle_db_exceptions
    def create_fund(db: Session, fund: Fund):
        """
        Creates a new fund in the database.

        :param db: Database session
        :param fund: Fund object to create
        :return: Created fund object
        """
        existing_fund = db.query(Fund).filter(Fund.name == fund["name"]).first()
        if existing_fund:
            raise HTTPException(
                status_code=400, detail="Fund with this name already exists"
            )
        db.add(fund)
        db.commit()
        db.refresh(fund)
        return fund

    @staticmethod
    @handle_db_exceptions
    def delete_fund(db: Session, fund_id: str):
        """
        Deletes a fund from the database by its ID.

        :param db: Database session
        :param fund_id: ID of the fund to delete
        :return: None
        :raises HTTPException: If fund is not found
        """
        fund = get_fund_or_404(db, fund_id)
        db.delete(fund)
        db.commit()

    @staticmethod
    @handle_db_exceptions
    def deactivate_fund(db: Session, fund_id: str):
        """
        Deactivates a fund by setting its 'is_active' flag to False.

        :param db: Database session
        :param fund_id: ID of the fund to deactivate
        :return: None
        :raises HTTPException: If the fund is not found
        """
        fund = get_fund_or_404(db, fund_id)
        fund.is_active = False
        db.commit()
        db.refresh(fund)
        return fund
