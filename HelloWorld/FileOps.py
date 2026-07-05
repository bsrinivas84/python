
from wsgiref import headers

from numpy import square


with open('test.csv','r') as f:
    headers = next(f)  # Skip the header line
    print("Squares of numbers in test.csv:")
    for line in f:
        print(square(int(line.strip())))