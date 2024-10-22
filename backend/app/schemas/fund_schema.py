from pydantic import BaseModel


class FundBase(BaseModel):
    name: str
    minimum_amount: float
    category: str


class FundCreate(FundBase):
    pass


class FundResponse(FundBase):
    id: str
    is_active: bool

    class Config:
        orm_mode = True
