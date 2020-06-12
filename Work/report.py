# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f"Row {row_no}: Bad row: {row}")
    return total_cost


def read_portfolio_(filename):
    '''
    Opens a given portfolio file and reads it into a list of tuples
    '''

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                print("Couldn't parse", row)

    return portfolio


def read_portfolio(filename):
    '''
    Opens a given portfolio file and reads it into a list of dictionaries
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            holding = dict(zip(headers, row))
            d = {
                'name' : holding['name'],
                'shares' : int(holding['shares']),
                'price' : float(holding['price'])
            }
            portfolio.append(d)

    return portfolio


def read_prices(filename):
    '''
    Reads a set of prices into a dictionary where the keys of the
    dictionary are the stock names and the values in the dictionary are the stock prices
    '''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) != 0:
                prices[row[0]] = float(row[1])

    return prices


def current_value(portfolio, prices):
    '''
    Computes current value of portfolio
    '''
    current_value = 0.0

    for i in portfolio:
        current_value += i['shares'] * prices[i['name']]

    return current_value


def make_report(portfolio, prices):
    '''
    Takes a list of stocks and dictionary of prices as input and
    returns a list of tuples containing the rows of the above table
    '''

    report = [] # list of tuples

    for stock in portfolio:
        t = (1,2)
        name = stock['name']
        shares = stock['shares']
        price = prices[name]
        change = price - stock['price']
        t = (name, shares, price, change)
        report.append(t)

    return report


def print_report(report):
    '''
    Prints out report
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    seperator = '---------- ---------- ---------- ----------'
    print(seperator)
    # print formatted report
    for name, shares, price, change in report:
        if price:
            price = '$' + str(price)
        print(f'{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Makes and prints out final report
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)

    return (print_report(report))


# file paths
file_portfolio = 'Data/portfolio.csv'
file_price = 'Data/prices.csv'

# call functions
portfolio_report(file_portfolio, file_price)








