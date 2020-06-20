# **Задание 3. **
# Напишите функцию, которая будет удалять все последовательные повторы слов из заданной строки
# при помощи регулярных выражений.

import re


def delete_dup(s):
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', s)


# test
print(delete_dup('one two two three four four'))
