"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""


def print_info(variable_list: list):
    """ Функция выводит тип и значение каждой переменной из переданного списка. """
    for variable in variable_list:
        print(f"Type: {type(variable)},\n"
              f"Value: {variable}\n")


VAR_1 = 'разработка'
VAR_2 = 'сокет'
VAR_3 = 'декоратор'
LIST_VAR = [VAR_1, VAR_2, VAR_3]

print_info(LIST_VAR)

VAR_1_UNI = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
VAR_2_UNI = '\u0441\u043e\u043a\u0435\u0442'
VAR_3_UNI = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
LIST_VAR_UNI = [VAR_1_UNI, VAR_2_UNI, VAR_3_UNI]

print_info(LIST_VAR_UNI)
