from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class ItemStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class ItemBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: ItemStatus = ItemStatus.PENDING
    priority: int = Field(default=1, ge=1, le=5)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    status: Optional[ItemStatus] = None
    priority: Optional[int] = Field(None, ge=1, le=5)


class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True