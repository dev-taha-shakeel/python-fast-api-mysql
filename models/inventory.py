
from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, index=True, autoincrement='auto')
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    date_updated = Column(DateTime(timezone=True), default=func.now())

    # Define relationship with Product
    product = relationship('Product', back_populates='inventory')
