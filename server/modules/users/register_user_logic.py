from returns.future import future_safe
from returns.io import IOResult
from returns.pipeline import flow

from server.database import engine
from server.documents.users import UserDoc


@future_safe
async def _save_user(user: UserDoc) -> UserDoc:
    return await engine.save(user)


async def register_user(
    telegram_id: int,
    username: str,
) -> IOResult[UserDoc, Exception]:
    return await flow(
        UserDoc(telegram_id=telegram_id, username=username),
        _save_user,
    )
