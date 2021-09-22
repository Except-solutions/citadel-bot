from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from server.settings.dev import settings

engine = AIOEngine(
    motor_client=AsyncIOMotorClient(
        settings.mongo_uri
    ),
    database='citadel',
)
