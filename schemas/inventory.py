from pydantic import BaseModel
from datetime import date

class InventoryBase(BaseModel):
    product_id: int
    quantity: int
    date_updated: date

class InventoryCreate(InventoryBase):
    pass

class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True