import datetime

#Variables
income = 0
expense = 0
miles = 0
hoursWorked = 0
dailyGoal = 240

#Inputs
income = input('Enter Income: ')
income = int(income)

expense = input('Do you have any Expense: ')
expense = int(expense)

miles = input('How many miles did you drive today: ')
miles = int(miles)

hoursWorked = input('How long did you grind today ')
hoursWorked = float(hoursWorked)

#Convertions
mileCost = miles * .23
dailyIncome = income - expense - mileCost
goalReached = dailyIncome - dailyGoal

hourly = dailyIncome/hoursWorked
perMile = income/miles
expense = expense + mileCost



# Date 
todayDate = datetime.datetime.now()

#Print out of inputs
print('\nOn', todayDate.strftime("%A"','),'Day',todayDate.strftime("%j"),'At',todayDate.strftime("%X"))
print('\nYou Entered', income, 'For Income')
print('You Entered', expense, 'For Expenses')
print('You Entered', miles, 'For Miles', 'With An Average Cost of: $', mileCost)
print('You Entered', hoursWorked, 'For Hours Worked')


print('\nYou made $',income, '\nWhile Spending: $',expense, '\nYou drove ', miles, 'miles. ')
print('\nYour Averages Are:',  '\nHourly: $', hourly, '\nWage Per Mile Driven: ', perMile,'\n')

print('$',goalReached)

#if statment - Did you reach your goal?
if income < dailyGoal:
    print('You Need To Grind Harder')
elif income > dailyGoal*2:
    print('Balling out of Control')
else:
    print('Good Job, Let Do Better Tommorow')

