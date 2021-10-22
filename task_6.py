"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet import detect


FILE_NAME = 'test_file.txt'
LINES = ['сетевое программирование', 'сокет', 'декоратор']


def write_in_file(file_name, lines):
    """Функция принимает список строк и записывает их в test_file """
    with open(file_name, 'w') as file:
        for line in lines:
            file.write(f'{line}\n')


def check_encode(file_name):
    """ Функция принимает название файла, открывает его и возвращает кодировку."""
    with open(file_name, 'rb') as file:
        content = file.read()
    encoding = detect(content)['encoding']
    return encoding


def force_open(file_name, encoding):
    """ Функция принимает название файла и кодировку,
    принудительно открывает файл в этой кодировке"""
    with open(file_name, 'r', encoding=encoding) as file:
        content = file.read()
        print(content)


write_in_file(FILE_NAME, LINES)
ENCODING = check_encode(FILE_NAME)
force_open(FILE_NAME, ENCODING)
