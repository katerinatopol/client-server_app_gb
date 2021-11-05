"""Unit-тесты клиента"""
import datetime
import sys
import os
import unittest

from common.status_codes import StatusCodes
from unit_tests.test_data import TRUE_REQUEST, CORRECT_200, CORRECT_400, NOT_CORRECT_ANS

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import generate_request, parse_request


class TestClient(unittest.TestCase):
    """ Класс с тестами """

    def setUp(self):
        print(f"Start test: {__name__} {datetime.datetime.now()}")

    def tearDown(self):
        print("End test")

    def test_correct_request(self):
        """Тест коректного запроса"""
        test_request = generate_request()
        test_request[TIME] = 1
        self.assertEqual(test_request, TRUE_REQUEST)

    def test_correct_200(self):
        """Тест корректного разбора ответа 200"""
        self.assertEqual(parse_request(StatusCodes.ok), CORRECT_200)

    def test_correct_400(self):
        """Тест корректного разбора 400"""
        self.assertEqual(parse_request(StatusCodes.bad_request_cl), CORRECT_400)

    def test_raises(self):
        """Тест исключения"""
        self.assertRaises(ValueError, parse_request, NOT_CORRECT_ANS)


if __name__ == '__main__':
    unittest.main()
