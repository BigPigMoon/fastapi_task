import uuid
import datetime

from app.models.product import ProductStorage, ProductOut, ProductIn, ProductDB
from prisma.models import Product


def convert_product_storage_to_out(product: ProductStorage) -> ProductOut:
    """Convert ProductStorage to ProductOut"""
    tmp_dict: dict = product.dict()
    tmp_dict.pop('secret_token', None)
    return ProductOut(**tmp_dict)


def convert_product_in_to_storage(product: ProductIn) -> ProductStorage:
    """Convert ProductIn to ProductStorage"""
    tmp_dict: dict = product.dict()
    return ProductStorage(
        id=uuid.uuid4(),
        create_at=datetime.datetime.now(),
        **tmp_dict
    )


def convert_product_in_to_db(product: ProductIn) -> ProductDB:
    tmp_dict: dict = product.dict()
    return ProductDB(
        create_at=datetime.datetime.now(),
        **tmp_dict
    )


def convert_product_db_to_out(product: ProductDB) -> ProductOut:
    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        create_at=product.create_at,
    )


def convert_product_prisma_to_out(product: Product) -> ProductOut:
    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        create_at=product.created_at
    )
