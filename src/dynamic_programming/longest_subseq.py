"""
Наибольшая последовательнократная подпоследовательность.

Дано целое число 1<=n<=10^3 и массив A[1...n] натуральных чисел, не превосходящих 2*10^9.
Выведите максимальное 1<=k<=n, для которого найдется подпоследовательность 1<=i1<=i2<=...<=ik<=n
длины k, в которой каждый элемент делится на предыдущий (формально:
для всех 1<=j<k, A[i_j] | A[i_j+1]
"""

import sys


def longest_subseq_len(arr) -> int:
    """
    Оптимальная подструктура задачи:
    Префикс оптимальной подпоследовательности тоже должен являться оптимальной подпосл-тью.
    Доказывается методом от противного: вырезать и вставить.
    """
    subseq_lens = [1] * len(arr)
    for i in range(1, len(arr)):
        max_prefix = -1
        # оптимальная подструктура задачи
        for j in range(i):
            if arr[i] % arr[j] == 0 and subseq_lens[j] > max_prefix:
                max_prefix = subseq_lens[j]
        if max_prefix != -1:
            subseq_lens[i] = max_prefix + 1
    return max(subseq_lens)


def run():
    reader = (map(int, line.split()) for line in sys.stdin)
    next(reader)
    arr = list(next(reader))
    print(longest_subseq_len(arr))


if __name__ == "__main__":
    run()
