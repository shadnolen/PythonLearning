income = 0
expense = 0
miles = 0
hoursWorked = 0

income = input('Enter Income: ')
income = int(income)

expense = input('Do you have any Expense: ')
expense = int(expense)

miles = input('How many miles did you drive today: ')
miles = int(miles)

hoursWorked = input('How long did you grind today ')
hoursWorked = int(hoursWorked)

dailyIncome = income - expense
hourly = dailyIncome/hoursWorked
perMile = income/miles

print(income)
print(expense)
print(miles)
print(hoursWorked)
print(dailyIncome)
print(hourly)
print(perMile)

print('You made $', income, 'and spent $', expense, 'and drove ', miles, 'miles. ')
print('Income - Expenses:', dailyIncome, 'Hourly Average: $', hourly, 'or made ', perMile, 'per mile!')
