from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True, autoincrement='auto')
    name = Column(String(100))
    description = Column(String(500))
    price = Column(Float)
    category = Column(String(100), index=True)

    # Define relationships
    inventory = relationship('Inventory', back_populates='product')
    sales = relationship('Sale', back_populates='product')
    historical_inventory = relationship('HistoricalInventory', back_populates='product')
