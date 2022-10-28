import json
import unittest
import socket
import core.var as var
import sys
import os
from core.utils import get_message, send_message
sys.path.append(os.path.join(os.getcwd(), '..'))


class TestUtils(unittest.TestCase):
    test_message = {
        'action': 'presence',
        'time': 1,
        'user': {
            'account_name': 'Guest'
        }
    }
    test_correct_response = {
        'response': 200
    }
    test_error_response = {
        'response': 400,
        'error': 'Bad Request'
    }

    # инициализируем тестовые сокеты для клиента и для сервера
    server_socket = None
    client_socket = None

    def setUp(self) -> None:
        # Создаем тестовый сокет для сервера
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((var.def_connect_adress, var.def_port))
        self.server_socket.listen(var.max_conn)
        # Создаем тестовый сокет для клиента
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((var.def_connect_adress, var.def_port))
        self.client, self.client_address = self.server_socket.accept()

    def tearDown(self) -> None:
        # Закрываем созданные сокеты
        self.client.close()
        self.client_socket.close()
        self.server_socket.close()

    def test_send_message_correct_message(self):
        """
        Проверяем отправку корректного сообщения
        """
        send_message(self.client_socket, self.test_message)
        test_response = self.client.recv(var.max_package)
        test_response = json.loads(test_response.decode(var.encod))
        self.assertEqual(test_response, self.test_message)

    def test_send_message_wrong_message(self):
        """
        Проверяем исключение, если на входе не словарь
        """
        self.assertRaises(TypeError, send_message, self.client_socket, 'not dict')

    def test_get_message_200(self):
        """
        Проверяем получение корректного сообщения
        """
        message = json.dumps(self.test_correct_response)
        self.client.send(message.encode(var.encod))
        response = get_message(self.client_socket)
        self.assertEqual(response, self.test_correct_response)

    def test_get_message_400(self):
        """
        Расшифровка ошибочного словаря
        """
        message = json.dumps(self.test_error_response)
        self.client.send(message.encode(var.encod))
        response = get_message(self.client_socket)
        self.assertEqual(response, self.test_error_response)

    def test_get_message_not_dict(self):
        """
        Возникновение ошибки, если пришедший объект не словарь
        """
        message = json.dumps('not dict')
        self.client.send(message.encode(var.encod))
        self.assertRaises(ValueError, get_message, self.client_socket)

    def test_get_message_dict(self):
        """
        Проверяем что возвращаемый объект словарь
        """
        message = json.dumps(self.test_correct_response)
        self.client.send(message.encode(var.encod))
        self.assertIsInstance(get_message(self.client_socket), dict)


if __name__ == '__main__':
    unittest.main()
