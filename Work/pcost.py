# pcost.py
#
# Exercise 1.27
import os

file_path = r"C:\Users\lingram\Desktop\practical-python-master\Work\Data\portfolio.csv"
f = open(file_path, 'rt')
header = next(f)

total_list = [] # empty list to store values of shares * price

for line in f:
    row = line.split(',')
    del row[0]

    for index, value in enumerate(row):
        row[index] = float(value)
        #f_string = f'Index = {index} \t value = {value}'
        #print(f_string)
        #print(type(row[index]))
    total_list.append(row[0] * row[1]) # add shares*price to total_list

f.close()

total = sum(total_list) # add values
print('Total cost', total)

# pcost.py
#
# Exercise 1.27
import os
import csv
import sys

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row_no, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                total_cost += shares*price
            except ValueError:
                print(f"Row {row_no}: Bad row: {row}")

    return total_cost  # add values


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)


# pcost.py
#
# Exercise 1.27
# using read_portfolio() function from report.py
import os
import csv
import sys
import report

def portfolio_cost(filename, select=['name','shares','price'], types=[str,int,float], has_headers=True):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename, select=select, types=types, has_headers=has_headers)
    total_cost = 0.0
    for stock in portfolio:
        total_cost += stock['shares'] * stock['price']

    return total_cost  # add values


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

















