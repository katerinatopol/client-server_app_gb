"""Программа-сервер"""
import logging
import socket
import sys
import json
import log.server_log_config
from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, RESPONDEFAULT_IP_ADDRESSSE
from common.utils import get_message, send_message

SERVER_LOG = logging.getLogger('server')


def check_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь -
    сообщение от клиента, проверяет корректность,
    возвращает словарь-ответ для клиента

    :param message:
    :return:
    """
    SERVER_LOG.debug(f'Принято сообщение от клиента: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'test_user':
        SERVER_LOG.debug('Ответ: {RESPONSE: 200}')
        return {RESPONSE: 200}

    SERVER_LOG.debug("Ответ: {RESPONDEFAULT_IP_ADDRESSSE: 400, ERROR: 'Bad Request'}")
    return {
        RESPONDEFAULT_IP_ADDRESSSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умоланию.
    Сначала обрабатываем порт:
    server.py -p [<port>] -a <addr>
    :return:
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
        SERVER_LOG.info(f'Порт для подключений: {listen_port}')
    except IndexError:
        SERVER_LOG.error('После параметра -\'p\' не указан номер порта.')
        sys.exit(1)
    except ValueError:
        SERVER_LOG.error(f'Указан адрес порта {listen_port}.'
                         f'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Затем загружаем какой адрес слушать

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
        SERVER_LOG.info(f'Адрес с которого принимаются подключения: {listen_address}.')
    except IndexError:
        SERVER_LOG.error('После параметра \'a\'- не указан адрес, который будет слушать сервер.')
        sys.exit(1)

    SERVER_LOG.info('Сервер запущен')

    # Готовим сокет

    SOCKET_SRV = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_SRV.bind((listen_address, listen_port))

    # Слушаем порт

    SOCKET_SRV.listen(MAX_CONNECTIONS)

    while True:
        SOCKET_CL, client_address = SOCKET_SRV.accept()
        SERVER_LOG.info(f'Установлено соедение: {client_address}')
        try:
            message_from_cient = get_message(SOCKET_CL)
            SERVER_LOG.debug(f'Получено сообщение от клиента: {message_from_cient}')
            response = check_message(message_from_cient)
            SERVER_LOG.info(f'Ответ сервера клиенту: {response}')
            send_message(SOCKET_CL, response)
            SOCKET_CL.close()
            SERVER_LOG.info(f'Закрыто соединение {client_address}.')
        except (ValueError, json.JSONDecodeError):
            SERVER_LOG.error('Принято некорретное сообщение от клиента.')
            SOCKET_CL.close()
            SERVER_LOG.info(f'Закрыто соединение {client_address}.')


if __name__ == '__main__':
    main()
