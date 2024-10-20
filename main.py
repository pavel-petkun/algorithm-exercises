import sys
from importlib import import_module

NUMBER_OF_ARGS = 2


def run_problem(module_name):
    try:
        run_function = getattr(import_module(f"src.{module_name}"), "run")
        run_function()
    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except AttributeError:
        print(f"Error: '{module_name}' doesn't have a 'run' function.")


if __name__ == "__main__":
    if len(sys.argv) != NUMBER_OF_ARGS:
        print("Usage: python main.py <problem_module_name>")
        sys.exit(1)
    run_problem(sys.argv[1])
