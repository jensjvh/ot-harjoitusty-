import unittest
import datetime
from utils.date_utils import convert_to_datetime


class TestDateUtils(unittest.TestCase):
    def setUp(self):
        self.datetime_str = "17.12.2024"
        self.datetime_obj = datetime.datetime(day=17, month=12, year=2024)

    def test_string_to_datetime(self):
        result_obj = convert_to_datetime(self.datetime_str)

        self.assertEqual(result_obj, self.datetime_obj)
