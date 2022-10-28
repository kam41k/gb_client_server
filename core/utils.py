import json
from core.var import max_package, encod


def get_message(client):
    encoded_response = client.recv(max_package)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(encod)
        if isinstance(json_response, str):
            response = json.loads(json_response)
            if isinstance(response, dict):
                return response
            raise ValueError
        raise ValueError
    raise ValueError


def send_message(socket, message):
    if not isinstance(message, dict):
        raise TypeError
    json_message = json.dumps(message)
    encoded_message = json_message.encode(encod)
    socket.send(encoded_message)
