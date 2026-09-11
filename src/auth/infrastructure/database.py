import os
import certifi
from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi
from beanie import init_beanie
from dotenv import load_dotenv

from .orm.models import UserModel

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "app_db")

client = AsyncMongoClient(
    MONGO_URI,
    server_api=ServerApi("1"),
    tlsCAFile=certifi.where(),
)


async def init_db():
    await client.admin.command("ping")
    await init_beanie(
        database=client[MONGO_DB_NAME],
        document_models=[UserModel],
    )
