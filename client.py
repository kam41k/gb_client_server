import sys
import json
import socket
import time
import core.var as var
from core.utils import get_message, send_message


def create_pres(account_name='Guest'):
    out = {
        'action': 'presence',
        'time': time.time(),
        'user': {
            'account_name': account_name
        }
    }
    return out


def get_response(message):
    if 'response' in message:
        if message['response'] == 200:
            return '200 : Connected'
        return f'400 : {message["error"]}'
    raise ValueError


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = var.def_connect_adress
        server_port = var.def_port
    except ValueError:
        print('Номер порта может быть от 1024 до 65535.')
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message = create_pres()
    send_message(client_socket, message)
    try:
        response = get_response(get_message(client_socket))
        print(response)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось распознать сообщение сервера.')


if __name__ == '__main__':
    main()
