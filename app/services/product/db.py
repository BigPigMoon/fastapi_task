from typing import List
import uuid
from sqlalchemy.orm import sessionmaker

from app.models.product import BaseProduct, ProductDB, ProductOut, ProductIn, engine, Base
from app.utils.product import convert_product_in_to_db, convert_product_db_to_out


class DatabaseProductService:
    """Базовый класс для функционала работы с продуктами"""

    def __init__(self) -> None:
        super().__init__()
        self.session = sessionmaker(engine)()

    def get_by_id(self, id: int) -> ProductOut | None:
        """Находит продукт по id"""
        product = self.session.query(ProductDB).filter(
            ProductDB.id == id).first()
        if product is None:
            return None
        return convert_product_db_to_out(product)

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """Находит все продукты"""
        products = []
        for product in self.session.query(ProductDB).all():
            products.append(convert_product_db_to_out(product))
        return products[skip:limit+skip]

    def create(self, product: ProductIn) -> ProductOut:
        """Создает продукт"""
        new_product = convert_product_in_to_db(product)
        self.session.add(new_product)
        self.session.commit()
        print(f'{new_product.id=}')
        return convert_product_db_to_out(new_product)

    def update(self, id: int, product: BaseProduct) -> ProductOut | None:
        """Обновляет информацию о продукте"""
        self.session.query(ProductDB).filter(ProductDB.id == id).update(
            {ProductDB.name: product.name, ProductDB.description: product.description}
        )
        self.session.commit()
        updated_product = self.session.query(
            ProductDB).filter(ProductDB.id == id).first()
        if updated_product is None:
            return None
        return convert_product_db_to_out(updated_product)

    def delete(self, id: int) -> ProductOut:
        """Удаляет продукт"""
        deleted_product = self.session.query(
            ProductDB).filter(ProductDB.id == id).first()
        self.session.query(ProductDB).filter(ProductDB.id == id).delete()
        self.session.commit()
        return deleted_product
