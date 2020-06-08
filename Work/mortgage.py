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


# mortgage.py
#
# Exercise 1.

# mortgage.py
# exercise 1.9

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    months+=1

print('Total paid', total_paid)
print('Total months', months)


# mortgage.py
#
# Exercise 1.

# mortgage.py
# exercise 1.10

extra_payment_start_month = 60
extra_payment_end_month = 107
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print(months+1, total_paid, principal)
    months+=1

print('Total paid', total_paid)
print('Total months', months)

# mortgage.py
# exercise 1.10

extra_payment_start_month = 60
extra_payment_end_month = 107
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    if principal < 0:
        total_paid = total_paid + principal
        principal = 0
    print(months+1, total_paid, principal)
    months+=1

print('Total paid', total_paid)
print('Total months', months)

