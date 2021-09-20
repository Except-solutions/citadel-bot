from random import randint

import httpx
from lambdas import _
from more_itertools import first
from returns.future import future_safe
from returns.io import IOResult, IOSuccess
from returns.pipeline import flow
from returns.unsafe import unsafe_perform_io

from server.settings.dev import settings

DEFAULT_PIC: str = f'boobs_preview/{settings.start_boob_id}.jpg'


@future_safe
async def _make_boobs_request(boob_id: str) -> list[dict[str, str]]:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(boob_id)
        response.raise_for_status()
        return response.json()


async def _get_random_boobs() -> IOResult[list[dict[str, str]], Exception]:
    return await flow(
        randint(settings.start_boob_id, settings.stop_boob_id),
        lambda boob_id: f'{settings.boobs_api}{boob_id}',
        _make_boobs_request,
    )


async def get_random_boobs() -> str:
    io_boobs = await _get_random_boobs()
    return unsafe_perform_io(
        io_boobs.lash(
            lambda _: IOSuccess([{'preview': DEFAULT_PIC}])
        ).map(
            lambda result: flow(
                result,
                first,
                _['preview'],
                lambda preview: f'http://media.oboobs.ru/{preview}',
            )
        ).unwrap()
    )
