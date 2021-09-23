import secrets
import datetime
from typing import List

from returns.future import future_safe
from returns.io import IOResult
from returns.pipeline import flow, pipe
from returns.io import IOSuccess, IOFailure, IOResult
from returns.pointfree import bind_ioresult
from returns.unsafe import unsafe_perform_io

from server.database import engine
from server.documents.fotd import FodtDoc
from server.documents.users import UserDoc
from server.utils import get_moscow_without_tz, get_yesterday


@future_safe
async def _get_register_users() -> List[UserDoc]:
    users = await engine.find(UserDoc)
    return users


async def _save_fotd_result(fotd: UserDoc) -> IOResult[UserDoc, Exception]:
    if today_fotd := await engine.find_one(
        FodtDoc,
        (FodtDoc.datetime > get_yesterday())
        & (FodtDoc.datetime < get_moscow_without_tz()),
    ):
        return IOFailure(today_fotd)
    saved_fodt = await engine.save(
        FodtDoc(user_doc=fotd, datetime=get_moscow_without_tz())
    )
    return IOSuccess(saved_fodt)


async def roll_fotd() -> IOResult[UserDoc, Exception]:
    register_users = await _get_register_users()
    return await unsafe_perform_io(register_users.map(
        secrets.choice
    ).map(
        IOSuccess
    ).map(
        bind_ioresult(_save_fotd_result)
    )).unwrap()
