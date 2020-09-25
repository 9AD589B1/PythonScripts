import csv
import random as rand
import string
from pathlib import Path
from random import choice


def rand_string():
    text = "".join(rand.choices(string.ascii_uppercase + string.digits, k=20))
    return text


def rand_integer():
    return rand.randint(1000000, 99999999)


func_list = [rand_string(), rand_integer()]
home = str(Path.home())
header_row = input("Enter number of columns to create: ")
rows = input("Enter number of rows to create: ")
delim = input("Enter delimiter: ")
file_name = input("Enter file name: ")
write_path = f"{home}/{file_name}.csv"

print("\nWriting test data delimited file...\n")

with open(write_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=delim)
    header = ["c" + str(i + 1) for i in range(int(header_row))]
    writer.writerow(header)
    for i in range(len(rows)):
        row = [choice(func_list) for i in range(int(header_row))]
        writer.writerow(row)

print("Test data writing complete!\n")