"""
Рюкзак 0-1 без ценности предметов.

Первая строка входа содержит целые числа 1<=W<=10^4 и 1<=n<=300 - вместимость рюкзака и число
золотых слитков.
Следующая строка содержит n целых чисел 0<=w1,...,wn<=10^5, задающих веса слитков. Найдите макс.
вес золота, который можно унести в рюкзаке.
"""

import sys


def knapsack_without_values(weights, max_weight) -> int:
    m = len(weights) + 1
    n = max_weight + 1

    table = [[0] * n for _ in range(m)]

    for i, w in enumerate(weights, 1):
        for j in range(1, n):
            if j - w >= 0:
                with_curr_item = table[i - 1][j - w] + w
            else:
                with_curr_item = 0
            without_curr_item = table[i - 1][j]

            table[i][j] = max(with_curr_item, without_curr_item)

    return table[-1][-1]


def run():
    reader = (map(int, line.split()) for line in sys.stdin)
    max_weight, _ = next(reader)
    weights = list(next(reader))
    print(knapsack_without_values(weights, max_weight))


if __name__ == "__main__":
    run()
