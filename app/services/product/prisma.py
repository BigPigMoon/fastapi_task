from typing import List

from app.models.product import ProductOut, ProductIn, BaseProduct
from app.utils.product import convert_product_prisma_to_out

from prisma.models import Product
from prisma import Prisma


class PrismaProductService:
    """Базовый класс для функционала работы с продуктами"""

    def __init__(self) -> None:
        self.database = Prisma()

    async def get_by_id(self, id: int) -> ProductOut | None:
        """Находит продукт по id"""
        await self.database.connect()
        product = await self.database.product.find_first(where={"id": id})
        await self.database.disconnect()
        if product is None:
            return None
        return convert_product_prisma_to_out(product)

    async def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """Находит все продукты"""
        products = []
        await self.database.connect()
        for product in await self.database.product.find_many():
            products.append(convert_product_prisma_to_out(product))
        await self.database.disconnect()
        return products

    async def create(self, product: ProductIn) -> ProductOut:
        """Создает продукт"""
        await self.database.connect()
        new_product: Product = await self.database.product.create({
            "name": product.name,
            "description": product.description,
            "secret_token": product.secret_token,
        })
        await self.database.disconnect()
        return convert_product_prisma_to_out(new_product)

    async def update(self, id: int, product: BaseProduct) -> ProductOut | None:
        """Обновляет информацию о продукте"""
        await self.database.connect()
        updated_product = await self.database.product.update(
            where={"id": id},
            data={
                "name": product.name,
                "description": product.description
            }
        )
        await self.database.disconnect()
        if updated_product is None:
            return None
        return convert_product_prisma_to_out(updated_product)

    async def delete(self, id: int) -> ProductOut | None:
        """Удаляет продукт"""
        await self.database.connect()
        deleted_product = await self.database.product.delete(where={"id": id})
        await self.database.disconnect()
        if deleted_product is None:
            return None
        return convert_product_prisma_to_out(deleted_product)
