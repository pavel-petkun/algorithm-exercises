"""
Лестница.

Даны число 1<=n<=100 ступенек лестницы и целые числа -10^4<=a1,...,an<=10^4, которыми помечены
ступеньки. Найдите макс. сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до
n-й ступеньки), каждый раз поднимаясь на 1 или 2 ступеньки.
"""

import sys


def max_sum_steps(steps):
    max_sum = [0, steps[0]]
    for i, step in enumerate(steps[1:], start=2):
        max_sum.append(max(max_sum[i - 2] + step, max_sum[i - 1] + step))
    return max_sum[-1]


def run():
    reader = (map(int, line.split()) for line in sys.stdin)
    next(reader)
    steps = list(next(reader))
    print(max_sum_steps(steps))


if __name__ == "__main__":
    run()
