import argparse
import csv

parser = argparse.ArgumentParser("day1")
parser.add_argument("input_file", help="The name of the file to parse.", type=str)
args = parser.parse_args()

def check_repeat(product_id):
    return product_id[:len(product_id) // 2] == product_id[len(product_id) // 2:]

password = 0
with open(args.input_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter=',')
    for row in reader:
        for entry in row:
            start, end = entry.split("-")
            for num in range(int(start), int(end)+1):
                if check_repeat(str(num)):
                    password += num

print(password)