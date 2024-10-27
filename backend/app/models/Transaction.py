import datetime
import enum
import uuid
from sqlalchemy import Column, String, Float, Enum, DateTime, func
from .Base import Base


class TransactionType(enum.Enum):
    SUBSCRIPTION = "subscription"
    CANCELLATION = "cancellation"


class Transaction(Base):
    __tablename__ = "transactions"

    type = Column(Enum(TransactionType), nullable=False)
    fund_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    code = Column(String, unique=True, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.code = self.generate_code(kwargs["fund_id"], kwargs["code"])

    @staticmethod
    def generate_code(fund_id: int, code: str) -> str:
        unique_suffix = uuid.uuid4().hex[:6]
        code_part = "".join(code.split()).upper()
        return f"{code_part}-{fund_id}-{unique_suffix}"
