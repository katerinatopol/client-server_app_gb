"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для
хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re

import chardet


def get_data():
    """ Функция осуществляет перебор файлов с данными, их открытие и считывание данных"""

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = []

    for num in range(1, 4):
        with open(f'info_{num}.txt', 'rb') as file:
            work_data = file.read()
            result = chardet.detect(work_data)
            data = work_data.decode(result['encoding'])

    regular_prod = re.compile(r'Изготовитель системы:\s*\S*')
    regular_name = re.compile(r'Windows\s*\S*')
    regular_code = re.compile(r'Код продукта:\s*\S*')
    regular_type = re.compile(r'Тип системы:\s*\S*')

    os_prod_list.append(regular_prod.findall(data)[0].split()[2])
    os_name_list.append(regular_name.findall(data)[0])
    os_code_list.append(regular_code.findall(data)[0].split()[2])
    os_type_list.append(regular_type.findall(data)[0].split()[2])

    heads = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(heads)

    work_data = [os_prod_list, os_name_list, os_code_list, os_type_list]

    for num in range(len(work_data[0])):
        work_row = list(map(lambda row: row[num], work_data))
        main_data.append(work_row)

    return main_data


def write_to_csv(link_to_file):
    """ Функция принимает ссылку на CSV-файл, реализует получение данных через вызов функции get_data()
    и сохраняет подготовленные данные в соответствующий CSV-файл """

    main_data = get_data()

    with open(link_to_file, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in main_data:
            writer.writerow(row)


write_to_csv('result.csv')
