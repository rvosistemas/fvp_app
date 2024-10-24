from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class TransactionTypeEnum(str, Enum):
    subscription = "subscription"
    cancellation = "cancellation"


class TransactionBase(BaseModel):
    type: TransactionTypeEnum
    fund_id: str
    amount: float


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
