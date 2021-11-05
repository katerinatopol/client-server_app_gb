"""Unit-тесты сервера"""
import datetime
import sys
import os
import unittest
from unit_tests.test_data import CORRECT_MESSAGE, BAD_USER, INSUFFICIENT_DATA
from server import check_message
from common.status_codes import StatusCodes

sys.path.append(os.path.join(os.getcwd(), '..'))


class TestServer(unittest.TestCase):

    def setUp(self):
        print(f"Start test: {__name__} {datetime.datetime.now()}")

    def tearDown(self):
        print("End test")

    def test_ok_check(self):
        """Корректный запрос"""
        self.assertEqual(check_message(CORRECT_MESSAGE), StatusCodes.ok)

    def test_insufficient_data(self):
        """Ошибка - не полные данные"""
        self.assertEqual(check_message(INSUFFICIENT_DATA), StatusCodes.bad_request_srv)

    def test_unknown_user(self):
        """ Ошибка - не test_user """
        self.assertEqual(check_message(BAD_USER), StatusCodes.bad_request_srv)


if __name__ == '__main__':
    unittest.main()
