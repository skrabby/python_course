# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки
# (если покупка была, сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты из файла
# visit_log.csv, в которых были покупки с указанием категории.
#
# Учтите условия на данные:
#
# содержимое purchase_log.txt помещается в оперативную память компьютера
# содержимое visit_log.csv - нет; используйте только построчную обработку этого файла


import json


def read_purchase_file(name):
    f = open(name, 'r', encoding="utf8")
    p = {}
    for line in f:
        obj = json.loads(line)
        p[obj['user_id']] = obj['category']
    return p


def check_visit_file(name, purchases):
    f = open(name, 'r', encoding="utf8")
    # fw = open('funnel.csv', 'w', encoding="utf8")
    # Не записывается кириллица

    fw = open('funnel.csv', 'w', encoding="utf16")  # Читается, но запятые не парсятся как делимитер
    for line in f:
        split = line.split(',')
        if split[0] in purchases:
            s = (split[0] + ', ' + split[1].rstrip('\n') + ', ' + purchases[split[0]] + '\n')
            fw.write(s)
    f.close()
    fw.close()


# driver code
purchases = read_purchase_file('purchase_log.txt')
check_visit_file('visit_log.csv', purchases)
