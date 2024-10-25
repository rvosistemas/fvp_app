from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session
from ..services.transaction_service import get_all_transactions, create_transaction
from ..schemas.transaction_schema import TransactionCreate, TransactionResponse
from ..docs.transaction_docs import transaction_create_example, transaction_responses
from ..config.database import get_db

router = APIRouter()


@router.get("/transactions", response_model=list[TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    """
    Retrieves a list of all transactions.
    """
    return get_all_transactions(db)


@router.post(
    "/transactions",
    response_model=TransactionResponse,
    status_code=201,
    responses=transaction_responses,
)
def create_new_transaction(
    transaction_data: TransactionCreate = Body(
        ..., examples=transaction_create_example
    ),
    db: Session = Depends(get_db),
):
    """
    Creates a new transaction in the database.

    Example:
    - **type**: Type of transaction (subscription or cancellation)
    - **fund_id**: ID of the fund associated with the transaction
    - **amount**: Amount of money for the transaction
    - **date**: Date of the transaction
    """
    return create_transaction(db, transaction_data.dict())
