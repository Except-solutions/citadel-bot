from os.path import splitext
from urllib.parse import urlparse

import httpx
from aiogram import types
from aiogram.utils.exceptions import BadRequest
from placeholder import _
from returns.future import future_safe
from returns.io import IOSuccess
from returns.unsafe import unsafe_perform_io
from tenacity import retry, retry_if_exception_type, stop_after_attempt

from server.settings.dev import settings

_IMAGE_EXTENSIONS = frozenset(('jpg', 'png', 'bmp', 'jpe', 'jpeg'))
_VIDEO_EXTENSIONS = frozenset(('webm', 'mp4', 'gif'))


def _get_file_ext_from(*, url: str) -> str:
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext[1:].lower()


@future_safe
async def _make_dog_request() -> dict[str, str]:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(settings.dogs_api)
        response.raise_for_status()
        return response.json()


async def get_random_dog() -> str:
    dog_io = await _make_dog_request()

    return unsafe_perform_io(dog_io.lash(lambda _: IOSuccess({'file': settings.default_dog})).map(_['url']).unwrap())


@retry(stop=stop_after_attempt(3), retry=retry_if_exception_type(BadRequest))
async def handle_random_dog_event(event: types.Message):
    url = await get_random_dog()
    ext = _get_file_ext_from(url=url)

    if ext in _IMAGE_EXTENSIONS:
        await event.reply_photo(photo=url)
    elif ext in _VIDEO_EXTENSIONS:
        await event.reply_video(video=url)
    else:
        await event.reply_document(document=url)
