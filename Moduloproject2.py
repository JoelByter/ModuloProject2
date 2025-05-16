import argparse
import os
parser = argparse.ArgumentParser(description="Process input data file.")
parser.add_argument("input_file", help="Path to the input data file")
args = parser.parse_args()
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    data = [float(line.strip()) for line in lines if line.strip().isdigit()]
    return data

def calculate_average(data):
    return sum(data) / len(data)

def calculate_maximum(data):
    return max(data)
 def write_output(data, average, maximum, output_file='output.txt'):
    with open(output_file, 'w') as file:
        file.write(f"Processed {len(data)} entries\n")
        file.write(f"Average: {average:.2f}\n")
        file.write(f"Maximum: {maximum:.2f}\n")
    data = read_data(args.input_file)
    if not data:
        raise ValueError("No valid data found.")
    avg = calculate_average(data)
    max_val = calculate_maximum(data)
    write_output(data, avg, max_val)
    print("Processing complete. Results written to output.txt")
except Exception as e:
    print(f"Error: {e}")
