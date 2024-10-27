from sqlalchemy import Column, String, Float, UniqueConstraint
from .Base import Base


class Fund(Base):
    __tablename__ = "funds"

    name = Column(String, index=True)
    minimum_amount = Column(Float)
    category = Column(String)

    __table_args__ = (UniqueConstraint("name", name="uq_fund_name"),)
