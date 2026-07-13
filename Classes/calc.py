
from myClass import MyClass

with open('..\HelloWorld\Data\companies.csv', 'r') as file:
    #file.__next__()  # Skip the header line
    lines = file.readlines()
    companies = []
    for line in lines[1:]:
        if line.strip().__len__() == 0:
            continue
        name, date, shares, price = line.strip().split(',')
        companies.append(MyClass(name, date, int(shares), float(price)))

    for company in companies:
        print(f'{getattr(company,"name")} on {getattr(company,"date")} has total value: {company.calc()}')
        if(company.name.strip("\"") == "MSFT"):
            setattr(company, "shares", 100)
            print(f'Updated {getattr(company,"name")} shares to {getattr(company,"shares")}')