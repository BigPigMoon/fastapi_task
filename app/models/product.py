import datetime
import uuid

from typing import Optional
from pydantic import BaseModel

from sqlalchemy import Column, String, Integer, DateTime, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///fastapi.db")
Base = declarative_base()


class ProductDB(Base):
    __tablename__ = "products"
    id = Column('id', Integer, primary_key=True, index=True)
    name = Column('name', String)
    description = Column('description', String)
    secret_token = Column('secret_token', String)
    create_at = Column('create_at', DateTime)
    # update_at = Column('update_at', DateTime)


Base.metadata.create_all(engine)


class BaseProduct(BaseModel):
    """Базовый класс продукта"""
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True


class ProductIn(BaseProduct):
    """Продукт, который приходит от пользователя"""
    secret_token: str


class ProductOut(BaseProduct):
    """Продукт, который отправляется пользователю"""
    id: uuid.UUID | int
    create_at: datetime.datetime


class ProductStorage(BaseProduct):
    """Продукт, который будет хравиться в хранилище"""
    id: uuid.UUID | int
    create_at: datetime.datetime
    secret_token: str
