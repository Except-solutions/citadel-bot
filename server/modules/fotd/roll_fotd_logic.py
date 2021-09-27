import secrets
from typing import List, Tuple

from returns.functions import raise_exception
from returns.future import future_safe
from returns.io import IO, IOResultE
from returns.unsafe import unsafe_perform_io

from server.database import engine
from server.documents.fotd import FodtDoc
from server.documents.users import UserDoc
from server.utils import get_moscow_without_tz, get_yesterday


class NotFoundFOTDError(Exception):
    """Exception if returned result []."""


class NotFoundRegisteredUsers(Exception):
    """Exception if returned result []."""


@future_safe
async def _get_registered_user() -> List[UserDoc]:
    if users := await engine.find(UserDoc):
        return users
    return raise_exception(NotFoundRegisteredUsers())


@future_safe
async def _get_today_fotd() -> FodtDoc:
    if today_fotd := await engine.find_one(
        FodtDoc,
        (FodtDoc.datetime > get_yesterday())
        & (FodtDoc.datetime < get_moscow_without_tz()),
    ):
        return today_fotd
    return raise_exception(NotFoundFOTDError())


@future_safe
async def _save_fotd_result(fotd: UserDoc) -> FodtDoc:
    return await engine.save(
        FodtDoc(user_doc=fotd, datetime=get_moscow_without_tz())
    )


@future_safe
async def roll_fotd() -> Tuple[bool, FodtDoc]:
    today_fotd: IOResultE[FodtDoc] = await _get_today_fotd()
    if today_fotd.value_or(None) == IO(None):
        result = await _get_registered_user()
        return True, unsafe_perform_io(
            (await result.map(secrets.choice).bind_ioresult(_save_fotd_result).awaitable()).unwrap()  # type: ignore
        )
    return False, unsafe_perform_io(today_fotd.unwrap())
