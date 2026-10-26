from contextlib import asynccontextmanager
from fastapi import FastAPI
from .auth.interface.auth_router import router as auth_router
from .auth.infrastructure.database import init_db
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://learn.localhost:3000",
        "http://127.0.0.1:3000",
        "https://sikkai.org",
        "https://learn.sikaai.org/"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Message": "Root"}
