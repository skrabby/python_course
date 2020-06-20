# Задание 1
# Напишите функцию, которая возвращает название валюты (поле ‘Name’)
# с максимальным значением курса с помощью сервиса https://www.cbr-xml-daily.ru/daily_json.js


import requests


def get_currency_max():
    full_data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    name = None
    max_value = 0
    val = full_data['Valute']
    for key, value in val.items():
        if value['Value'] > max_value:
            max_value = value['Value']
            name = value['Name']
    return name


# test
print(get_currency_max())
