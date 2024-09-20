"""
Восстановите строку по её коду и префиксному коду символов.

В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
встречающихся в строке, и размер получившейся закодированной строки, соответственно.
В следующих k строках записаны коды букв в формате "letter: code". Ни один код не является префиксом другого.
Буквы могут быть перечислены в любом порядке. В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
каждая из этих букв встречается в строке хотя бы один раз.
Наконец, в последней строке записана закодированная строка.
Исходная строка и коды всех букв непусты. Заданный код таков, что закодированная строка имеет минимальный возможный
размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит 10^4 символов.
"""

import sys


def decode(s: str, lettercode_dict: dict[str, str]) -> str:
    codeletter_dict = {code: letter for letter, code in lettercode_dict.items()}
    decoded_str = ""
    idx = 0
    while idx < len(s):
        code = s[idx]
        while code not in codeletter_dict:
            idx += 1
            code += s[idx]
        decoded_str += codeletter_dict[code]
        idx += 1
    return decoded_str


def main():
    alphabet_size, _ = map(int, sys.stdin.readline().split())
    lettercode_dict = {}
    for i in range(alphabet_size):
        letter, code = tuple(e.strip() for e in sys.stdin.readline().split(":"))
        lettercode_dict[letter] = code
    encoded_str = sys.stdin.readline().strip()
    print(decode(encoded_str, codeletter_dict))


if __name__ == "__main__":
    main()
