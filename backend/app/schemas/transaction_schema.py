from pydantic import BaseModel
from enum import Enum


class TransactionTypeEnum(str, Enum):
    subscription = "subscription"
    cancellation = "cancellation"


class TransactionBase(BaseModel):
    type: TransactionTypeEnum
    fund_id: str
    amount: float
    date: str


class TransactionCreate(TransactionBase):
    pass


class TransactionResponse(TransactionBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True
