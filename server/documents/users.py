from odmantic import AIOEngine, Field, Model
from pymongo import ASCENDING, TEXT


class UserDoc(Model):
    telegram_id: int
    username: str
    is_admin: bool = False


async def user_doc_index(engine: AIOEngine):
    await engine.client['citadel']['user_doc'].create_index(
        [('telegram_id', ASCENDING)],
        background=True,
        unique=True
    )
    await engine.client['citadel']['user_doc'].create_index(
        [('username', TEXT)],
        background=True,
        unique=True
    )
