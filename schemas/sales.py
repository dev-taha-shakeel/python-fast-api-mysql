from pydantic import BaseModel
from datetime import date

class SaleBase(BaseModel):
    product_id: int
    quantity_sold: int
    sale_amount: float
    sale_date: date
    category: str

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int

    class Config:
        orm_mode = True