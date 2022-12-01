from fastapi import FastAPI

from app.routers import product


def set_routers(app: FastAPI):
    app.include_router(product.router, prefix="", tags=['products'])
