"""
Pydantic schemas for news app
"""

from datetime import datetime

from pydantic import BaseModel


class CategoryReadSchema(BaseModel):
    """
    Category read schema
    """
    id: int
    name: str
    created: datetime

    class Config:
        orm_mode = True


class CategoryCreateSchema(BaseModel):
    """
    Category create schema
    """
    name: str