import socket
import sys
import json
import core.var as var
from core.utils import get_message, send_message


def prep_response(message):
    if 'action' in message and message['action'] == 'presence' and 'time' in message \
            and 'user' in message and message['user']['account_name'] == 'Guest':
        return {'response': 200}
    return {
        'response': 400,
        'error': 'Bad Request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = var.def_port
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -p необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('Номер порта может быть от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print(
            'После параметра -a необходимо указать адрес.')
        sys.exit(1)

    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv_socket.bind((listen_address, listen_port))
    serv_socket.listen(var.max_conn)

    while True:
        client_socket, client_address = serv_socket.accept()
        try:
            message = get_message(client_socket)
            print(message)
            response = prep_response(message)
            send_message(client_socket, response)
            client_socket.close()
        except (ValueError, json.JSONDecodeError):
            client_socket.close()


if __name__ == '__main__':
    main()
