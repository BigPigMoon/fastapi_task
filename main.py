import uvicorn
from app.core import settings
from fastapi import FastAPI
from app.core.router import set_routers


app = FastAPI()


@app.on_event("startup")
async def startup():
    set_routers(app)


@app.on_event("shutdown")
async def shutdown():
    pass

if __name__ == "__main__":
    uvicorn.run('main:app', port=settings.PORT,
                host=settings.HOST, reload=True)
