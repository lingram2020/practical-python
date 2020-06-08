# mortgage.py
#
# Exercise 1.8

# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
payment_year_1 = 3684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months < 12:
        principal = principal * (1 + rate / 12) - payment_year_1
        total_paid = total_paid + payment_year_1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    months+=1

print('Total paid', total_paid)
print('Total months', months)
