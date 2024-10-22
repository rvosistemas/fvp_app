from sqlalchemy import Column, String, Float, Enum
from app.models.Base import Base
import enum


class TransactionType(enum.Enum):
    SUBSCRIPTION = "subscription"
    CANCELLATION = "cancellation"


class Transaction(Base):
    __tablename__ = "transactions"

    type = Column(Enum(TransactionType), nullable=False)
    fund_id = Column(String)
    amount = Column(Float)
    date = Column(String)
