def read_portfolio(file_path):
    """
    Reads a CSV file containing portfolio data and returns a list of dictionaries.
    
    Each dictionary represents a row in the CSV file, with keys corresponding to the column headers.
    
    :param file_path: Path to the CSV file.
    :return: List of dictionaries representing the portfolio data.
    """
    import csv
    
    portfolio_data = []
    stock_sum = 0.0
    with open(file_path, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            portfolio_data.append(row)
            stock_sum += float(row['price']) * int(row['shares'])
    
    return portfolio_data, stock_sum

item, totalPrice = read_portfolio('companies.csv')
print(f"Total price of the portfolio: {totalPrice}")