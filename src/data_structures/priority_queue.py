"""
Очередь с приоритетом.

Первая строка входа содержит число операций 1<=n<=10^5. Каждая из последующих n строк задают
операцию одного из следующих двух типов:
Insert x, где 0<=x<=10^9 - целое число;
ExtractMax

Первая операция добавляет число x в очередь с приоритетами, вторая – извлекает максимальное число
и выводит его.
"""

import sys
from dataclasses import dataclass
from typing import Sequence


@dataclass
class Node:
    index: int
    priority: int


class Heap:
    def __init__(self):
        self.arr = []

    def insert(self, priority: int):
        self.arr.append(priority)
        self._sift_up()

    def extract_max(self) -> int:
        max_priority = self.arr[0]
        self._sift_down()
        return max_priority

    def _sift_up(self):
        priority = self.arr[-1]
        current_idx = len(self.arr) - 1
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2
            if priority > self.arr[parent_idx]:
                self._arr_swap(current_idx, parent_idx)
                current_idx = parent_idx
            else:
                break

    def _sift_down(self):
        if len(self.arr) == 0:
            return
        if len(self.arr) == 1:
            self.arr.pop()
            return

        self.arr[0] = self.arr.pop()
        priority = self.arr[0]
        current_index = 0
        while True:
            left_idx = 2 * current_index + 1
            right_idx = 2 * current_index + 2

            child_nodes = [
                Node(
                    index=left_idx,
                    priority=self.arr[left_idx] if left_idx < len(self.arr) else -1,
                ),
                Node(
                    index=right_idx,
                    priority=self.arr[right_idx] if right_idx < len(self.arr) else -1,
                ),
            ]

            max_child = max(child_nodes, key=lambda node: node.priority)
            if priority < max_child.priority:
                self._arr_swap(current_index, max_child.index)
                current_index = max_child.index
            else:
                break

    def _arr_swap(self, idx1: int, idx2: int):
        self.arr[idx1], self.arr[idx2] = self.arr[idx2], self.arr[idx1]


def perform_operations(operations: Sequence[Sequence[str]]) -> list[int]:
    max_elements = []
    heap = Heap()
    for op in operations:
        match op:
            case ["Insert", elem]:
                heap.insert(int(elem))
            case ["ExtractMax"]:
                max_elements.append(heap.extract_max())
    return max_elements


def run():
    n = int(sys.stdin.readline())
    operations = list(line.split() for line in sys.stdin)
    assert n == len(operations)
    max_elements = perform_operations(operations)

    for elem in max_elements:
        print(elem)


if __name__ == "__main__":
    run()
