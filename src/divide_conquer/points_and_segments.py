"""
Точки и отрезки.

В первой строке задано 2 числа 1<=n<=50000 и 1<=m<=50000 - кол-во отрезков и точек на прямой,
соответственно. Следующие n строк содержат по 2 целых числа ai и bi (ai <= bi) - координаты
концов отрезков. Последняя строка содержит m целых чисел - координаты точек. Все координаты
не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него
или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она
принадлежит.
"""

import bisect
import sys
from random import randint


def _qsort_partition(arr: list[int], lo: int, hi: int) -> tuple[int, int]:
    # select a pivot element x = arr[p]
    p = randint(lo, hi)

    # place pivot element into the first position
    arr[lo], arr[p] = arr[p], arr[lo]

    u = j = lo
    # keeping the following invariant:
    # arr[k]<x for lo+1<=k<=j; arr[k]=x for j+1<=k<=u; arr[k]>x for u+1<=k<=i
    for i in range(lo + 1, hi + 1):
        if arr[i] < arr[lo]:
            arr[u + 1], arr[i] = arr[i], arr[u + 1]
            arr[j + 1], arr[u + 1] = arr[u + 1], arr[j + 1]
            u += 1
            j += 1
        elif arr[i] == arr[lo]:
            arr[u + 1], arr[i] = arr[i], arr[u + 1]
            u += 1

    arr[lo], arr[j] = arr[j], arr[lo]  # put a pivot element into the proper position

    return j, u


def qsort(arr: list[int], lo: int, hi: int):
    if lo < hi:
        m, u = _qsort_partition(arr, lo, hi)
        qsort(arr, lo, m - 1)
        qsort(arr, u + 1, hi)


def segments_cover(l_segments: list[int], r_segments: list[int], points: list[int]) -> list[int]:
    # Although we could use the optimized built-in Timsort algorithm,
    # we'll implement Quick Sort from scratch.
    qsort(l_segments, 0, len(l_segments) - 1)
    qsort(r_segments, 0, len(r_segments) - 1)

    cover_counts = []
    for point in points:
        l_idx = bisect.bisect_right(l_segments, point)
        r_idx = bisect.bisect_left(r_segments, point)
        # Note that
        # A and B = A \ (Omega \ B), where Omega = A or B, so the number of segments = l_idx - r_idx
        cover_counts.append(l_idx - r_idx)

    return cover_counts


def run():
    reader = (map(int, line.split()) for line in sys.stdin)
    num_segments, num_points = next(reader)
    l_segm, r_segm = map(list, zip(*(tuple(next(reader)) for _ in range(num_segments))))
    points = list(next(reader))

    assert len(l_segm) == len(r_segm)

    print(*segments_cover(l_segm, r_segm, points))


if __name__ == "__main__":
    run()
