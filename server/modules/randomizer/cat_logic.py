import httpx
from placeholder import _
from returns.future import future_safe
from returns.io import IOSuccess
from returns.unsafe import unsafe_perform_io

from server.settings.dev import settings


@future_safe
async def _make_cat_request() -> dict[str, str]:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(settings.cats_api)
        response.raise_for_status()
        return response.json()


async def get_random_cat() -> str:
    cat_io = await _make_cat_request()
    return unsafe_perform_io(cat_io.lash(lambda _: IOSuccess({'file': settings.default_cat})).map(_['file']).unwrap())
