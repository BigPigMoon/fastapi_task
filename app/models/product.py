import datetime
import uuid

from typing import Optional
from pydantic import BaseModel


class BaseProduct(BaseModel):
    """Базовый класс продукта"""
    name: str
    description: Optional[str] = None


class ProductIn(BaseProduct):
    """Продукт, который приходит от пользователя"""
    secret_token: str


class ProductOut(BaseProduct):
    """Продукт, который отправляется пользователю"""
    id: uuid.UUID
    create_at: datetime.datetime


class ProductStorage(BaseProduct):
    """Продукт, который будет хравиться в хранилище"""
    id: uuid.UUID
    create_at: datetime.datetime
    secret_token: str
