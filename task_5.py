"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
"""

import subprocess
from chardet import detect

RESOURCES = ['yandex.ru', 'youtube.com']


def ping(web):
    PING = subprocess.Popen(('ping', web), stdout=subprocess.PIPE)
    for count, line in enumerate(PING.stdout):
        res = detect(line)
        line = line.decode(res['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        if count == 5:
            break


for resource in RESOURCES:
    ping(resource)
