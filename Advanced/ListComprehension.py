#Use List comprehension 
import csv
import urllib.error
import urllib.request
from pathlib import Path


myList = [1,2,3,4,5]

squareList = [x*x for x in myList]
#print(squareList)

csv_path = Path(__file__).resolve().parent.parent / 'HelloWorld' / 'Data' / 'companies.csv'
companyName = []
names = ''
with open(csv_path, 'r') as f:
    reader = csv.DictReader(f)
    portfolio_data = []
    stock_sum = 0.0
    for row in reader:
        portfolio_data.append(row)
        companyName.append(row['name'])

    stock_sum = sum([float(p['price']) * int(p['shares']) for p in portfolio_data])
    print(f"Total price of the portfolio: {stock_sum}")

    names = ', '.join(companyName)
    print(f"Company names: {names}")

    names = ','.join(companyName)
    url = 'https://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(names)
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        if err.code == 429:
            print('Yahoo request was rate-limited (HTTP 429). Try again later.')
        else:
            print(f'HTTP error while fetching quotes: {err}')
    except urllib.error.URLError as err:
        print(f'Network error while fetching quotes: {err}')


