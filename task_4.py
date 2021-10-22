"""
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

VAR_1 = 'разработка'
VAR_2 = 'администрирование'
VAR_3 = 'protocol'
VAR_4 = 'standard'
LIST_VAR = [VAR_1, VAR_2, VAR_3, VAR_4]


def encode_var(variable_list):
    """
    Функция принимает список слов в строковом представлении, преобразовывает каждое из них
    и возвращает список слов в байтовом представлении.
    """
    b_var_list = []
    for var in variable_list:
        b_var_list.append(var.encode('utf-8'))
    return b_var_list


def decode_var(variable_list):
    """
    Функция принимает список слов в байтовом представлении, преобразовывает каждое из них
    и возвращает список слов в строковом представлении.
    """
    s_var_list = []
    for var in variable_list:
        s_var_list.append(var.decode('utf-8'))
    return s_var_list


print(LIST_VAR)
LIST_VAR_B = encode_var(LIST_VAR)
print(LIST_VAR_B)
LIST_VAR_S = decode_var(LIST_VAR_B)
print(LIST_VAR_S)
