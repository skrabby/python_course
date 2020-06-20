# # Домашнее задание
# 1. Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# ```python
# {'1840e0b9d4': 'Продукты', ...}
# ```

import json


def read_file_dir(name):
    f = open(name, 'r', encoding="utf8")
    purchases = {}
    for line in f:
        obj = json.loads(line)
        purchases[obj['user_id']] = obj['category']
    return purchases


# test
print(read_file_dir('purchase_log.txt'))
