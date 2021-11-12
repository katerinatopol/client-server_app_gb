import logging
import log.server_log_config
import log.client_log_config
import sys

LOGGER_NAME = sys.argv[0].split('.')[0]
LOGGER = logging.getLogger(LOGGER_NAME)


def logger(func):
    def my_logger(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.debug(f'Имя вызываемой функции: {func.__name__}; параметры: {args}, {kwargs}.')
        return result
    return my_logger
