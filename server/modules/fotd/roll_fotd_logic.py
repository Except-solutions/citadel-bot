import secrets
import datetime
from typing import List

from returns.functions import raise_exception
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


class NotFoundFOTDError(Exception):
    ...


async def _get_register_users() -> List[UserDoc]:
    return await engine.find(UserDoc)


async def _get_today_fotd() -> FodtDoc:
    if today_fotd := await engine.find_one(
        FodtDoc,
        (FodtDoc.datetime > get_yesterday())
        & (FodtDoc.datetime < get_moscow_without_tz()),
    ):
        return today_fotd
    return IOFailure('FOTD not found')


async def _save_fotd_result(fotd: UserDoc) -> IOResult[UserDoc, Exception]:
    saved_fodt = await engine.save(
        FodtDoc(user_doc=fotd, datetime=get_moscow_without_tz())
    )
    return IOSuccess(saved_fodt)


@future_safe
async def make_io() -> FodtDoc:
    if today_fotd := await _get_today_fotd():
        return today_fotd
    register_users = await _get_register_users()
    return await unsafe_perform_io(register_users.map(
        secrets.choice
    ).map(
        IOSuccess
    ).map(
        bind_ioresult(_save_fotd_result)
    )).unwrap()


async def roll_fotd() -> IOResult[UserDoc, Exception]:
    today_fotd = await make_io()
    return
