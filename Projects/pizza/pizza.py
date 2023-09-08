import sys
import csv
from tabulate import tabulate

#out put if less the two comman line arguest
if len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

table =[]


if len(sys.argv) == 2:
    filename = sys.argv[1]
    if filename.endswith(".csv"):
        with open(filename, "r") as file:
            for row in file:
                stripped = row.rstrip().split(",")
                table.append(stripped)
        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    else:
        sys.exit("Not a CSV file")
