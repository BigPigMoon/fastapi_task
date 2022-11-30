import uuid
import datetime

from ..models.product import ProductStorage, ProductOut, ProductIn


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
