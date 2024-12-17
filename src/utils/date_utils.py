import datetime


DATE_FORMAT = '%d.%m.%Y'


def convert_to_datetime(date_string: str) -> datetime.datetime:
    return datetime.datetime.strptime(date_string, DATE_FORMAT)


def convert_datetime_to_string(datetime_object: datetime.datetime) -> str:
    return datetime_object.strftime(DATE_FORMAT)
