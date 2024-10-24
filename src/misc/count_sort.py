"""
Сортировка подсчетом.

Первая строка содержит число 1<=n<=10^4, вторая - n натуральных чисел, не превышающих 10.
Выведите упорядоченную по неубыванию последовательность этих чисел.
"""

import sys


def count_sort(arr: list[int], max_element: int) -> list[int]:
    cums = [0] * (max_element + 1)
    for e in arr:
        cums[e] += 1

    for i in range(2, max_element + 1):
        cums[i] += cums[i - 1]

    res_arr = [0] * (len(arr) + 1)
    for i in range(len(arr) - 1, -1, -1):
        res_arr[cums[arr[i]]] = arr[i]
        cums[arr[i]] -= 1

    return res_arr[1:]


def run():
    reader = (map(int, line.split()) for line in sys.stdin)
    next(reader)
    arr = list(next(reader))
    print(*count_sort(arr, 10))


if __name__ == "__main__":
    run()
