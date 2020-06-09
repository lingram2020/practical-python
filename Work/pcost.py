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



