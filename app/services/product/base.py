from typing import List
import uuid

from app.models.product import ProductIn, ProductOut, BaseProduct


class BaseProductService:
    """Базовый класс для функционала работы с продуктами"""

    async def get_by_id(self, id: uuid.UUID | int) -> ProductOut | None:
        """Находит продукт по id"""
        raise NotImplementedError

    async def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """Находит все продукты"""
        raise NotImplementedError

    async def create(self, product: ProductIn) -> ProductOut | None:
        """Создает продукт"""
        raise NotImplementedError

    async def update(self, id: uuid.UUID | int, product: BaseProduct) -> ProductOut | None:
        """Обновляет информацию о продукте"""
        raise NotImplementedError

    async def delete(self, id: uuid.UUID | int) -> ProductOut | None:
        """Удаляет продукт"""
        raise NotImplementedError
