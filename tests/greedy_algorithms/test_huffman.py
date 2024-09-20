import pytest

from greedy_algorithms import huffman_encoding, huffman_decoding


@pytest.fixture
def resources_root():
    return "../../resources/greedy_algorithms"


def test_encode(resources_root):
    with open(resources_root + "/input/huffman_encoding_input2.txt") as file:
        original_str = file.read().strip()

    with open(resources_root + "/output/huffman_encoding_output2.txt") as file:
        alphabet_size, _ = map(int, file.readline().split())
        codes_dict_expected = {}
        for i in range(alphabet_size):
            letter, code = tuple(e.strip() for e in file.readline().split(":"))
            codes_dict_expected[letter] = code
        encoded_str_expected = file.readline().strip()

    codes_dict_actual, encoded_str_actual = huffman_encoding.encode(original_str)

    assert codes_dict_expected == codes_dict_actual
    assert encoded_str_expected == encoded_str_actual


def test_encode_decode(resources_root):
    with open(resources_root + "/input/huffman_encoding_input2.txt") as file:
        original_str = file.read().strip()

    codes_dict, encoded_str = huffman_encoding.encode(original_str)
    assert original_str == huffman_decoding.decode(encoded_str, codes_dict)
