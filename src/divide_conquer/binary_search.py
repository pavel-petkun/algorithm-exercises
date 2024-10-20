"""
Двоичный поиск.

В первой строке даны целое число 1 <= n <= 10^5 и массив A[1...n] из n натуральный чисел,
не превышающих 10^9, в порядке возрастания, во второй - целое число 1 <= k <= 10^5 и k натуральных
чисел b1, ... bk, не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс
1 <= j <= n, для которого A[j]=bi, или -1, если такого j нет.
"""

import bisect
import sys


def search(sorted_list, elems_to_search):
    indices = []
    for e in elems_to_search:
        idx = bisect.bisect_left(sorted_list, e)
        if idx < len(sorted_list) and e == sorted_list[idx]:
            indices.append(idx + 1)  # 1-based index
        else:
            indices.append(-1)
    return indices


def run():
    _, *sorted_list = map(int, sys.stdin.readline().split())
    _, *elements_to_search = map(int, sys.stdin.readline().split())
    indices = search(sorted_list, elements_to_search)
    print(*indices)


if __name__ == "__main__":
    run()
