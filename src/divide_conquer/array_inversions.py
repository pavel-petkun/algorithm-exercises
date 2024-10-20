"""
Число инверсий.

Первая строка содержит число 1 <= n <= 10^5, вторая - массив A[1...n] из n натуральный чисел,
не превышающих 10^9.
Необходимо посчитать число пар индексов 1 <= i < j <= n, для которых A[i] > A[j].

Такая пара элементов называется инверсией массива. Количество инверсий в массиве является
в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве
инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые 2 элемента.
"""

import sys
from dataclasses import dataclass


@dataclass
class SortedArrayWithInv:
    arr: list[int]
    inv_count: int


def _merge(o1: SortedArrayWithInv, o2: SortedArrayWithInv) -> SortedArrayWithInv:
    inv_count = o1.inv_count + o2.inv_count
    res_arr = []
    arr1, arr2 = o1.arr, o2.arr

    p1 = p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            res_arr.append(arr1[p1])
            p1 += 1
        else:
            res_arr.append(arr2[p2])
            inv_count += len(arr1) - p1
            p2 += 1
    if p1 < len(arr1):
        res_arr.extend(arr1[p1:])
    if p2 < len(arr2):
        res_arr.extend(arr2[p2:])

    return SortedArrayWithInv(arr=res_arr, inv_count=inv_count)


def merge_sort_extended(arr: list[int], lo: int, hi: int) -> SortedArrayWithInv:
    # lo <= e < hi
    if hi - lo < 2:
        return SortedArrayWithInv(arr=[arr[lo]], inv_count=0)
    mid = (lo + hi) // 2
    return _merge(merge_sort_extended(arr, lo=lo, hi=mid), merge_sort_extended(arr, lo=mid, hi=hi))


def run():
    reader = (line for line in sys.stdin)
    next(reader)
    arr = list(map(int, next(reader).split()))
    print(merge_sort_extended(arr, lo=0, hi=len(arr)).inv_count)


if __name__ == "__main__":
    run()
