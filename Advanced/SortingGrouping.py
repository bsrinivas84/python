#Sorting 1

import csv
from pathlib import Path


def holding_name(holding):
    return holding['name']

portfolio_data = []
csv_path = Path(__file__).resolve().parent.parent / 'HelloWorld' / 'Data' / 'companies.csv'
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        portfolio_data.append(row)

print(portfolio_data)
portfolio_data.sort(key=holding_name)
print(portfolio_data)

print("=========================================")
#Sorting 2

lambda_portfolio_data = []
csv_path = Path(__file__).resolve().parent.parent / 'HelloWorld' / 'Data' / 'companies.csv'
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        lambda_portfolio_data.append(row)

print(lambda_portfolio_data)
lambda_portfolio_data.sort(key=lambda holding: holding['name'])
print(lambda_portfolio_data)