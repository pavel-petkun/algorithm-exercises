import subprocess

import pytest

from utils import find_io_file_pairs

RESOURCES_ROOT = "data/data_structures/priority_queue"
PROBLEM_MODULE_NAME = "src.data_structures.priority_queue"


def run_test(input_filepath, output_filepath, module_name):
    with open(input_filepath) as file:
        completed_process = subprocess.run(
            ["python", "-m", module_name], stdin=file, capture_output=True, text=True
        )
        actual_res = completed_process.stdout.strip()

    with open(output_filepath) as file:
        expected_res = file.read().strip()

    assert actual_res == expected_res


test_cases = find_io_file_pairs(RESOURCES_ROOT)


@pytest.mark.parametrize("input_filepath, output_filepath", test_cases)
def test_cases(input_filepath, output_filepath):
    run_test(input_filepath, output_filepath, PROBLEM_MODULE_NAME)
