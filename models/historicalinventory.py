from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class HistoricalInventory(Base):
    __tablename__ = 'historical_inventory'

    id = Column(Integer, primary_key=True, autoincrement='auto')
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    date_updated = Column(DateTime(timezone=True), default=func.now())

    # Define relationship with Product
    product = relationship('Product', back_populates='historical_inventory')