from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True, autoincrement='auto')
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity_sold = Column(Integer)
    sale_amount = Column(Float)
    sale_date = Column(Date)
    category = Column(String(100), index=True)
    comments = Column(String(500))

    # Define relationship
    product = relationship('Product', back_populates='sales')