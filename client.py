"""Программа-клиент"""

import sys
import json
import socket
import time
import logging
import log.client_log_config
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, \
    RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, PORT
from common.utils import get_message, send_message
from errors import ReqFieldMissingError

CLIENT_LOG = logging.getLogger('client')


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
    CLIENT_LOG.debug(f'Сгенерирован запрос {request}\nо присутствии клиента {account_name}')
    return request


def parse_request(message):
    """ Функция разбирает ответ сервера """
    CLIENT_LOG.debug(f'Разбор сообщения от сервера: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            CLIENT_LOG.debug("Возвращен ответ '200 : OK'")
            return '200 : OK'
        CLIENT_LOG.debug(f"Возвращен ответ '400 : {message[ERROR]}'")
        return f'400 : {message[ERROR]}'
    CLIENT_LOG.error(ReqFieldMissingError(RESPONSE))
    raise ReqFieldMissingError(RESPONSE)


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
        CLIENT_LOG.warning('Недостаточно данных, клиент будет запущен с дефолтными значениями порта и адреса.')
        SERVER_PORT = DEFAULT_PORT
        SERVER_ADDR = DEFAULT_IP_ADDRESS

    except ValueError:
        CLIENT_LOG.error(
            f'Попытка запуска клиента с неподходящим номером порта: {SERVER_PORT}.'
            f' Допустимы адреса с 1024 до 65535.')
        sys.exit(1)

    CLIENT_LOG.info(f'Запущен клиент с парамертами: '
                    f'адрес сервера: {SERVER_ADDR} , порт: {SERVER_PORT}')

    # Инициализация сокета и обмен

    SOCKET_CL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_CL.connect((SERVER_ADDR, SERVER_PORT))
    client_message = generate_request(SERVER_PORT)
    send_message(SOCKET_CL, client_message)
    CLIENT_LOG.debug(f'Отправлено сообщение {client_message}')
    try:
        server_response = parse_request(get_message(SOCKET_CL))
        CLIENT_LOG.info(f'Ответ сервера {server_response}')
        SOCKET_CL.close()
        CLIENT_LOG.info(f'Закрыто соединение {SERVER_ADDR}.')

    except (ValueError, json.JSONDecodeError):
        CLIENT_LOG.error('Не удалось декодировать сообщение сервера.')
        SOCKET_CL.close()
        CLIENT_LOG.info(f'Закрыто соединение {SERVER_ADDR}.')

    except ReqFieldMissingError as missing_error:
        CLIENT_LOG.error(f'В ответе сервера отсутствует необходимое поле {missing_error.missing_field}')
        SOCKET_CL.close()
        CLIENT_LOG.info(f'Закрыто соединение {SERVER_ADDR}.')

    except ConnectionRefusedError:
        CLIENT_LOG.critical(f'Не удалось подключиться к серверу {SERVER_ADDR}:{SERVER_PORT}, '
                            f'конечный компьютер отверг запрос на подключение.')


if __name__ == '__main__':
    main()
