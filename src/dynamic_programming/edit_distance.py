"""
Расстояние редактирования.

Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2, содержащих
строчные буквы латинского алфавита.
"""

import sys


def edit_distance(s1, s2) -> int:
    prev = list(range(len(s2) + 1))

    for i, ch1 in enumerate(s1, 1):
        curr = [i] + [0] * (len(s2))
        for j, ch2 in enumerate(s2, 1):
            add_dist = curr[j - 1] + 1
            del_dist = prev[j] + 1
            repl_dist = prev[j - 1] + (ch1 != ch2)

            curr[j] = min(add_dist, del_dist, repl_dist)
        prev = curr.copy()

    return prev[-1]


def run():
    str1, str2 = (line.strip() for line in sys.stdin)
    print(edit_distance(str1, str2))


if __name__ == "__main__":
    run()
