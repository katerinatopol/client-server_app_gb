"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.
"""


def print_info(variable_list: list):
    """ Функция выводит тип, содержимое и длину каждой переменной из переданного списка. """
    for variable in variable_list:
        print(f"Type : {type(variable)},\n"
              f"Value: {variable},\n"
              f"Length: {len(variable)}\n")


VAR_1 = b'class'
VAR_2 = b'function'
VAR_3 = b'method'
LIST_VAR = [VAR_1, VAR_2, VAR_3]

print_info(LIST_VAR)
