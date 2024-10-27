from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.fund_service import (
    get_funds,
    get_fund_by_id,
    create_fund,
    delete_fund,
    deactivate_fund,
)
from ..schemas.fund_schema import FundCreate, FundResponse
from ..docs.fund_docs import fund_create_example, fund_responses
from ..config.database import get_db

router = APIRouter()


@router.get("/funds", response_model=list[FundResponse])
def list_funds(db: Session = Depends(get_db)):
    """
    Retrieves a list of all funds.
    """
    return get_funds(db)


@router.get("/funds/{fund_id}", response_model=FundResponse)
def get_fund(fund_id: str, db: Session = Depends(get_db)):
    """
    Retrieves a fund by its ID.
    """
    fund = get_fund_by_id(db, fund_id)
    if not fund:
        raise HTTPException(status_code=404, detail="Fund not found")
    return fund


@router.post(
    "/funds", response_model=FundResponse, status_code=201, responses=fund_responses
)
def create_new_fund(
    fund_data: FundCreate = Body(..., examples=fund_create_example),
    db: Session = Depends(get_db),
):
    """
    Creates a new fund in the database.

    Example:
    - **name**: Name of the fund
    - **minimum_amount**: Minimum investment amount
    - **category**: Category of the fund
    """
    return create_fund(db, fund_data.dict())


@router.delete("/funds/{fund_id}", status_code=204)
def remove_fund(fund_id: str, db: Session = Depends(get_db)):
    """
    Deletes a fund by its ID.
    """
    return delete_fund(db, fund_id)


@router.patch("/funds/{fund_id}/deactivate", response_model=FundResponse)
def deactivate_fund_route(fund_id: str, db: Session = Depends(get_db)):
    """
    Deactivates a fund by setting its 'is_active' flag to False.

    :param fund_id: ID of the fund to deactivate
    :param db: Database session
    :return: Deactivated fund object
    """
    return deactivate_fund(db, fund_id)
