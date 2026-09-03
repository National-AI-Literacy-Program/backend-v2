from contextlib import asynccontextmanager
from fastapi import FastAPI
from .auth.interface.auth_router import router as auth_router
from .auth.infrastructure.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)



@app.get("/")
async def root():
    return {"Mandeep Bhandari": "Benevolent dictator for life"}
