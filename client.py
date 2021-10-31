"""Программа-клиент"""

import sys
import json
import socket
import time
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, PORT
from common.utils import get_message, send_message


def generate_request(server_port=DEFAULT_PORT, account_name='test_user'):
    """ Функция генерирует запрос о присутствии клиента """

    #  {'action': 'presence', 'time': 1634873801.598524, 'port': 9000, 'user': {'account_name': 'Guest'}}
    request = {
        ACTION: PRESENCE,
        TIME: time.time(),
        PORT: server_port,
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return request


def parse_request(message):
    """ Функция разбирает ответ сервера """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """
    Запуск из командной строки:
    client.py [<port>] <addr>
    """

    try:
        SERVER_PORT = int(sys.argv[1])
        SERVER_ADDR = sys.argv[2]

        if SERVER_PORT < 1024 or SERVER_PORT > 65535:
            raise ValueError
    except IndexError:
        SERVER_PORT = DEFAULT_PORT
        SERVER_ADDR = DEFAULT_IP_ADDRESS

    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен

    SOCKET_CL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_CL.connect((SERVER_ADDR, SERVER_PORT))
    client_message = generate_request(SERVER_PORT)

    send_message(SOCKET_CL, client_message)
    try:
        server_response = parse_request(get_message(SOCKET_CL))
        print(server_response)
        SOCKET_CL.close()
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')
        SOCKET_CL.close()


if __name__ == '__main__':
    main()
