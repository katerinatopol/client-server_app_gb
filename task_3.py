"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'
LIST_VAR = [VAR_1, VAR_2, VAR_3, VAR_4]


def check_encode(variable_list):
    """
    Функция принимает список слов и пробует каждое из них перевести в байтовый тип.
    Выводит слова, которые не удалось перевести в байтовый тип.
    """
    not_encode = []
    for var in variable_list:
        try:
            bytes(var, 'ascii')
        except UnicodeEncodeError as err:
            not_encode.append(var)
    if len(not_encode) > 0:
        print(f"Невозможно записать в байтовом типе: {' ,'.join(not_encode)}")
    else:
        print("Все слова можно записать в байтовом типе")


check_encode(LIST_VAR)
