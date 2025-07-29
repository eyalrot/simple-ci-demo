from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime

from app.models import Item, ItemCreate, ItemUpdate, ItemStatus

router = APIRouter()

fake_db = {}
counter = 0


@router.post("/", response_model=Item, status_code=201)
async def create_item(item: ItemCreate):
    global counter
    counter += 1
    
    now = datetime.utcnow()
    db_item = Item(
        id=counter,
        **item.dict(),
        created_at=now,
        updated_at=now
    )
    
    fake_db[counter] = db_item
    return db_item


@router.get("/", response_model=List[Item])
async def get_items(
    status: Optional[ItemStatus] = Query(None, description="Filter by status"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):
    items = list(fake_db.values())
    
    if status:
        items = [item for item in items if item.status == status]
    
    return items[skip : skip + limit]


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return fake_db[item_id]


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    stored_item = fake_db[item_id]
    update_data = item_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(stored_item, field, value)
    
    stored_item.updated_at = datetime.utcnow()
    return stored_item


@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    
    del fake_db[item_id]
    return None