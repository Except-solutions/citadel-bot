import httpx
from placeholder import _
from returns.future import future_safe
from returns.io import IOResult, IOSuccess
from returns.pipeline import flow
from returns.unsafe import unsafe_perform_io

from server.settings.dev import settings


@future_safe
async def _make_anime_request(url: str) -> dict[str, str]:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()


async def _get_random_anime(category: str) -> IOResult[dict[str, str], Exception]:
    return await flow(
        category,
        lambda anime: f'{settings.anime_api}{anime}',
        _make_anime_request,
    )


async def get_random_anime(category: str) -> str:
    cat_io = await _get_random_anime(category)
    return unsafe_perform_io(cat_io.lash(lambda _: IOSuccess({'url': settings.default_anime})).map(_['url']).unwrap())
