# Задание 1.
# Напишите функцию, которая принимает на вход строку и проверяет является ли она валидным транспортным номером.
# Если да, то функция должна возвращать отдельно номер и регион.

import re


def valid_transport_number(number):
    match = re.match("^[A-Z0-9]*-[0-9]*-[A-Z]*$", number)
    if match is not None:
        split = number.split('-')
        return [re.sub("[^0-9]", "", split[0]), split[1]]
    print('Введен неверный формат. Пример ввода: P777MK-70-RUS')


# test
arr = valid_transport_number('P777MK-70-RUS')
print(arr)
