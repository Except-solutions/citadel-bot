from lambdas import _
from random import randint
from asyncio import get_event_loop
import httpx
from more_itertools import first
from returns.future import future_safe, Future
from returns.io import IOResultE
from returns.pipeline import flow

from server.settings.dev import settings

DEFAULT_PIC = 'http://api.oboobs.ru/boobs/1'


def sync_request(coro):
    return Future(coro.awaitable)


@future_safe
async def _make_request_boobs() -> IOResultE[str]:
    return flow(
        randint(0, 10330),
        lambda boob_id: f'{settings.boobs_api}{boob_id}',
        httpx.Client().get,
        sync_request,  #  Todo unwrap Future and continue flow
        first,
        _['preview']
    )


async def get_random_boobs():
    io_boobs_result = await _make_request_boobs()
    return io_boobs_result.lash(
        lambda _: IOSuccess(DEFAULT_PIC),  # type: ignore
    ).compose_result(
        lambda pic_url: f'http://media.oboobs.ru/{pic_url.unwrap()}',  # type: ignore
    )
