from random import randint

import httpx
from lambdas import _
from more_itertools import first
from returns.future import future_safe
from returns.io import IOResult, IOSuccess
from returns.pipeline import flow
from returns.unsafe import unsafe_perform_io

from server.settings.dev import settings

DEFAULT_PIC: str = f'{settings.butts_media}/butts_preview/0569.jpg'


@future_safe
async def _make_butt_request(butt_id: str) -> list[dict[str, str]]:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(butt_id)
        response.raise_for_status()
        return response.json()


async def _get_random_butt() -> IOResult[list[dict[str, str]], Exception]:
    return await flow(
        randint(settings.start_butt_id, settings.stop_butt_id),
        lambda butt_id: f'{settings.butts_api}/{butt_id}',
        _make_butt_request,
    )


async def get_random_butt() -> str:
    io_butts = await _get_random_butt()
    return unsafe_perform_io(
        io_butts.lash(
            lambda _: IOSuccess([{'preview': DEFAULT_PIC}])
        ).map(
            lambda result: flow(
                result,
                first,
                _['preview'],
                lambda preview: f'{settings.butts_media}/{preview}',
            )
        ).unwrap()
    )
