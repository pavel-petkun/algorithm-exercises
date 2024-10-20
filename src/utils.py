import glob
import os


def find_io_file_pairs(data_dir):
    input_files = glob.glob(os.path.join(data_dir, "input*.txt"))
    file_pairs = []
    for input_file in input_files:
        # Extract the number from the input file name
        number = input_file.split("input")[-1].split(".txt")[0]
        output_file = os.path.join(data_dir, f"output{number}.txt")
        if os.path.exists(output_file):
            file_pairs.append((input_file, output_file))
    return file_pairs
