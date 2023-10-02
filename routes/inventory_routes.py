from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_session
from models.inventory import Inventory
from models.historicalinventory import HistoricalInventory

router = APIRouter()

@router.get("/inventory/{product_id}", response_model=Inventory)
def get_current_inventory(product_id: int, db: Session = Depends(get_session)):
    """
    Get the current inventory status for a specific product.
    """
    inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()
    if inventory is None:
      raise HTTPException(status_code=404, detail='Inventory not found against product_id: {product_id}')
    return inventory

@router.get("/inventory/low-stock-alerts", response_model=list[Inventory])
def get_low_stock_alerts(threshold: int = 10, db: Session = Depends(get_session)):
    """
    Get a list of products with low stock levels (below a specified threshold).
    """
    low_stock_products = db.query(Inventory).filter(Inventory.quantity < threshold).all()
    return low_stock_products

@router.put("/inventory/{product_id}")
def update_inventory(product_id: int, quantity_change: int, db: Session = Depends(get_session)):
    """
    Update inventory levels for a specific product and track the change over time.
    """
    product_inventory = db.query(Inventory).filter(Inventory.product_id == product_id).first()

    if product_inventory:
        # Update the current inventory level
        product_inventory.quantity += quantity_change

        # Create a historical inventory record for tracking changes
        historical_inventory = HistoricalInventory(
            product_id=product_id,
            quantity=quantity_change,
        )

        # Add historical inventory record to the database
        db.add(historical_inventory)
        db.commit()

        return {"message": "Inventory updated successfully"}

    return {"message": "Product not found"}
