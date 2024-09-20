"""
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
постройте оптимальный префиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке, и размер получившейся закодированной строки.
В следующих k строках запишите коды букв в формате "letter: code". В последней строке выведите закодированную строку.
"""

import heapq
from collections import Counter
from dataclasses import dataclass
from functools import total_ordering


@dataclass
@total_ordering
class Node:
    freq: int
    left: "Node" = None
    right: "Node" = None
    letter: str = None
    code: str = ""

    @classmethod
    def from_childnodes(cls, left: "Node", right: "Node"):
        return cls(freq=left.freq + right.freq, left=left, right=right)

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def traverse(self, codes_dict: dict, accum_code: str):
        accum_code = accum_code + self.code
        if self.left and self.right:
            self.left.traverse(codes_dict, accum_code)
            self.right.traverse(codes_dict, accum_code)
        else:
            codes_dict[self.letter] = accum_code


def codes_tree(s: str) -> Node:
    letterfreq_heap = [
        Node(freq=freq, letter=letter) for letter, freq in Counter(s).items()
    ]
    heapq.heapify(letterfreq_heap)

    if len(letterfreq_heap) == 1:
        return Node(
            freq=letterfreq_heap[0].freq, letter=letterfreq_heap[0].letter, code="0"
        )

    while len(letterfreq_heap) > 1:
        # make a greedy step
        min_node1 = heapq.heappop(letterfreq_heap)
        min_node2 = heapq.heappop(letterfreq_heap)
        min_node1.code = "0"
        min_node2.code = "1"
        heapq.heappush(
            letterfreq_heap, Node.from_childnodes(left=min_node1, right=min_node2)
        )
    return letterfreq_heap[0]


def encode(s: str) -> tuple[dict[str, str], str]:
    root_node = codes_tree(s)
    codes_dict = {}
    root_node.traverse(codes_dict, "")
    encoded_str = "".join((codes_dict[letter] for letter in s))
    return codes_dict, encoded_str


def main():
    input_str = input()
    lettercode_dict, encoded_str = encode(input_str)
    print(f"{len(lettercode_dict)} {len(encoded_str)}")
    for letter, code in lettercode_dict.items():
        print(f"{letter}: {code}")
    print(encoded_str)


if __name__ == "__main__":
    main()
