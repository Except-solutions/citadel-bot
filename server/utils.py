import datetime


def get_moscow_without_tz() -> datetime.datetime:
    return datetime.datetime.now() + datetime.timedelta(hours=3)


def get_yesterday() -> datetime.datetime:
    return get_moscow_without_tz() - datetime.timedelta(days=1)
