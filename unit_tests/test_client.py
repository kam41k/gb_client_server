import unittest
import sys
import os
from client import create_pres, get_response
sys.path.append(os.path.join(os.getcwd(), '..'))


class TestClient(unittest.TestCase):
    def test_def_pres_create(self):
        """Тест создания корректного запроса без указания account_name"""
        test = create_pres()
        test['time'] = 1
        self.assertEqual(test, {'action': 'presence', 'time': 1, 'user': {'account_name': 'Guest'}})

    def test_user_pres_create(self):
        """Тест создания корректного запроса с указанием account_name"""
        test = create_pres('User')
        test['time'] = 1
        self.assertEqual(test, {'action': 'presence', 'time': 1, 'user': {'account_name': 'User'}})

    def test_200_response(self):
        """Тест разбора ответа 200"""
        self.assertEqual(get_response({'response': 200}), '200 : Connected')

    def test_400_response(self):
        """Тест разбора ответа 400"""
        self.assertEqual(get_response({'response': 400, 'error': 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест разбора ответа без поля response"""
        self.assertRaises(ValueError, get_response, {'error': 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
