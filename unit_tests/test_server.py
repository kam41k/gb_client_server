import unittest
import sys
import os
from server import prep_response
sys.path.append(os.path.join(os.getcwd(), '..'))


class TestServer(unittest.TestCase):
    err_response = {'response': 400, 'error': 'Bad Request'}

    def test_correct_message(self):
        """Тест создания ответа, при корректном запросе"""
        self.assertEqual(prep_response({'action': 'presence', 'time': 1,
                                        'user': {'account_name': 'Guest'}}), {'response': 200})

    def test_no_action(self):
        """Тест создания ответа, в запросе нет действия"""
        self.assertEqual(prep_response({'time': 1, 'user': {'account_name': 'Guest'}}), self.err_response)

    def test_wrong_action(self):
        """Тест создания ответа, в запросе некорректное действие"""
        self.assertEqual(prep_response({'action': 'wrong', 'time': 1,
                                        'user': {'account_name': 'Guest'}}), self.err_response)

    def test_no_time(self):
        """Тест создания ответа, в запросе нет времени"""
        self.assertEqual(prep_response({'action': 'presence',
                                        'user': {'account_name': 'Guest'}}), self.err_response)

    def test_no_user(self):
        """Тест создания ответа, в запросе нет пользователя"""
        self.assertEqual(prep_response({'action': 'presence', 'time': 1}), self.err_response)

    def test_wrong_user(self):
        """Тест создания ответа, в запросе некорректный пользователь"""
        self.assertEqual(prep_response({'action': 'presence', 'time': 1,
                                        'user': {'account_name': 'User'}}), self.err_response)


if __name__ == '__main__':
    unittest.main()
