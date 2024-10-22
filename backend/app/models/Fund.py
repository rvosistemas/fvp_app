from sqlalchemy import Column, String, Float
from app.models.Base import Base


class Fund(Base):
    __tablename__ = "funds"

    name = Column(String, index=True)
    minimum_amount = Column(Float)
    category = Column(String)
