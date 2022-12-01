from typing import List
from fastapi import APIRouter, Depends
import uuid

from ..models.product import ProductIn, ProductOut, BaseProduct, ProductStorage
from ..services.product.base import BaseProductService
from ..dependencies import get_product_service


router = APIRouter()


@router.get("/products", response_model=List[ProductOut])
async def get_products(
        product_service: BaseProductService = Depends(get_product_service),
        limit: int = 100,
        skip: int = 0,
):
    return await product_service.get_all(limit, skip)


@router.get("/product/{id}", response_model=ProductOut | None)
async def get_product(
        id: uuid.UUID | int,
        product_service: BaseProductService = Depends(get_product_service),
):
    return await product_service.get_by_id(id)


@router.post("/product", response_model=ProductOut)
async def create_product(
        product_in: ProductIn,
        product_service: BaseProductService = Depends(get_product_service)
):
    return await product_service.create(product_in)


@router.put("/product", response_model=ProductOut | None)
async def update_product(
        id: uuid.UUID | int,
        base_product: BaseProduct,
        product_service: BaseProductService = Depends(get_product_service)
):
    return await product_service.update(id, base_product)


@router.delete("/product", response_model=ProductOut | None)
async def delete_product(
        id: uuid.UUID | int,
        product_service: BaseProductService = Depends(get_product_service)
):
    return await product_service.delete(id)
