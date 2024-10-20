## Algorithmic problems in Python

This repository contains my solutions to various problems, 
focusing on data structures and algorithm design using Python.

The problems are from the Stepik course:
[Алгоритмы: теория и практика. Методы](https://stepik.org/course/217)

---

## Setup

Create a virtual environment and setup dependencies from requirements.txt

`pip install -r requirements.txt`

Make sure you are in the project's root directory before running the commands below.

### Run a Problem Solution

To run a specific solution, use the following command format:

`python main.py <module_name>`

**Example:**
`python main.py divide_conquer.array_inversions`

#### Run a Solution with input from a file

`python main.py <module_name> < <input_filepath>`

For **Windows PowerShell**, use:
`Get-Content <input_filepath> | python main.py <module_name>`

**Example** (Windows PowerShell):
`Get-Content data\divide_conquer\array_inversions\input1.txt | python main.py divide_conquer.array_inversions`

---

### Code Formatting and Linting

#### Code formatter (`black`)

To format the code according to the black configuration:

`black --config pyproject.toml .`

#### Linter (`ruff`):
To check for linting issues:
`ruff check .` 

To automatically fix errors:
`ruff check . --fix`

To only fix import-related issues:
`ruff check . --fix --select=I`

### Running Tests
To run all tests using pytest:
`pytest`
