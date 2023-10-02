from pydantic import BaseModel
from datetime import date

class HistoricalInventoryBase(BaseModel):
    product_id: int
    quantity: int
    date_updated: date

class HistoricalInventoryCreate(HistoricalInventoryBase):
    pass

class HistoricalInventory(HistoricalInventoryBase):
    id: int

    class Config:
        orm_mode = True