from typing import Dict, List
import uuid
from app.models.product import BaseProduct, ProductDB, ProductOut, ProductIn, ProductStorage
from app.utils.product import convert_product_in_to_storage, convert_product_storage_to_out
from app.services.product.base import BaseProductService


class ProductTmpService(BaseProductService):
    """Temp service for product
    store data in dict, do not save after reload!!!"""

    def __init__(self) -> None:
        super().__init__()
        self.storage: Dict[uuid.UUID, ProductStorage] = {}

    def get_by_id(self, id: uuid.UUID) -> ProductOut | None:
        """Находит продукт по id"""
        product: ProductStorage | None = self.storage.get(id)
        if product is None:
            return None
        return convert_product_storage_to_out(product)

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """Находит все продукты"""
        product_list = []
        for _, product in self.storage.items():
            product_list.append(product)
        return product_list[skip:limit+skip]

    def create(self, product: ProductIn) -> ProductOut:
        """Создает продукт"""
        new_product = convert_product_in_to_storage(product)
        self.storage.update({new_product.id: new_product})
        return convert_product_storage_to_out(new_product)

    def update(self, id: uuid.UUID, new_product: BaseProduct) -> ProductOut | None:
        """Обновляет информацию о продукте"""
        product: ProductStorage | None = self.storage.get(id)
        if product is None:
            return None
        product.name = new_product.name
        product.description = new_product.description
        self.storage.update({product.id: product})
        return convert_product_storage_to_out(product)

    def delete(self, id: uuid.UUID) -> ProductOut | None:
        """Удаляет продукт"""
        product: ProductStorage | None = self.storage.pop(id, None)
        if product is None:
            return None
        return convert_product_storage_to_out(product)
