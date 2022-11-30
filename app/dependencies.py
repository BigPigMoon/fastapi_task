from app.services.product import ProductTmpService


TMP_SERVICE = ProductTmpService()


def get_product_service():
    """get product service"""
    return TMP_SERVICE
