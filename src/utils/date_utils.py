import datetime


DATE_FORMAT = '%d.%m.%Y'


def convert_to_datetime(date_string: str) -> datetime.datetime:
    return datetime.datetime.strptime(date_string, DATE_FORMAT)
