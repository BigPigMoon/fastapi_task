from app.services.product.db import DatabaseProductService
from app.services.product.prisma import PrismaProductService
from app.services.product.tmp import ProductTmpService


TMP_SERVICE = ProductTmpService()
DB_SERVICE = DatabaseProductService()
PRISMA_SERVICE = PrismaProductService()


async def get_product_service():
    """get product service"""
    return PRISMA_SERVICE
