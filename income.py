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

daliyIncome = income - expense
hourly = daliyIncome/hoursWorked
perMile = miles/income


print(income , daliyIncome, hourly, perMile)