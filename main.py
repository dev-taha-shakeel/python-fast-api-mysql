from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud
from database import SessionLocal, engine

from models import product, sales, inventory, historicalinventory

# product.Base.metadata.create_all(bind=engine)
# sales.Base.metadata.create_all(bind=engine)
# inventory.Base.metadata.create_all(bind=engine)
# historicalinventory.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
async def root():
    return {"message": "Hello World"}