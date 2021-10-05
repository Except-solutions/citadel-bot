from typing import TypedDict, cast

import httpx
from aiogram import types
from placeholder import _
from returns.functions import raise_exception
from returns.future import future_safe
from returns.io import IOResultE
from returns.pipeline import flow
from returns.unsafe import unsafe_perform_io

from server.modules.dvach.constants import BOARDS_LIST, SortType
from server.settings.dev import settings


class _Thread(TypedDict):
    comment: str
    lasthit: int
    num: str
    posts_count: int
    score: float
    subject: str
    timestamp: int
    views: int


class _BoardThreads(TypedDict):
    board: str
    threads: list[_Thread]


@future_safe
async def _make_threads_request(url: str) -> _BoardThreads:
    async with httpx.AsyncClient(timeout=5) as client:
        response = await client.get(url)
        response.raise_for_status()
        return cast(_BoardThreads, response.json())


async def _get_board_threads(board_id: str) -> IOResultE[_BoardThreads]:
    return await flow(
        f'{settings.dvach_url}/{board_id}/threads.json',
        _make_threads_request,
    )


def _sort_threads(threads: list[_Thread], sort_type: SortType):
    return sorted(threads, key=_[sort_type.name], reverse=True)


def _parse_args(raw_args: str) -> tuple[str, SortType, int]:
    args = raw_args.split()

    board_id = args[0] if args else 'b'

    try:
        sort_type = SortType[args[1]]
    except (IndexError, KeyError):
        sort_type = SortType.views

    try:
        limit = int(args[2])
    except (IndexError, ValueError):
        limit = 5

    return board_id, sort_type, limit


def _prepare_message_threads_rows(threads: list[_Thread], board_id: str, limit: int) -> list[str]:
    rows = []
    for num, thread in enumerate(threads, 1):
        rows.append(
            '{0}) <a href="https://2ch.hk/{5}/res/{6}.html">{1} ({2}; {3:.2f}; {4})</a>'.format(
                num, thread['subject'], thread['views'], thread['score'], thread['posts_count'], board_id, thread['num']
            )
        )
        if num == limit:
            break

    return rows


async def handle_top_event(event: types.Message) -> None:
    board_id, sort_type, limit = _parse_args(event.get_args())

    if board_id not in BOARDS_LIST:
        await event.reply(f'Неизвестная доска: {board_id}')
        return

    board_threads = await _get_board_threads(board_id)

    sorted_threads = (
        board_threads.alt(raise_exception).map(_['threads']).map(lambda threads: _sort_threads(threads, sort_type))
    )

    threads_rows = unsafe_perform_io(
        sorted_threads.map(lambda threads: _prepare_message_threads_rows(threads, board_id, limit)).unwrap()
    )

    header_rows = [
        f'<strong>Доска:</strong> {board_id}',
        f'<strong>Метод сортировки:</strong> {sort_type.value}\n',
    ]

    msg = '\n'.join([*header_rows, *threads_rows])

    await event.reply(msg, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
