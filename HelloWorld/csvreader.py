import csv

from numpy import square

def cubes(x):
    return x ** 3

with open('test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header line
    print("Cubes of numbers in test.csv:")
    for row in reader:
        prin(cubes(int(row[0]))) #No need of stripping as csv.reader handles that automatically