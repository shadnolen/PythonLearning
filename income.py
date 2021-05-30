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
expenseTotal = expense + mileCost

# Let's Round two decmial places 
incomeRound = round(income, 2)
expenseRound = round(expense, 2)
hourlyRound = round(hourly, 2)
milesRound = round(perMile, 2)
milesCostRound = round(mileCost,2)
goalReached = round(goalReached, 2)
# Date 
todayDate = datetime.datetime.now()

#Print out of inputs
print('\nOn', todayDate.strftime("%A"','),'Day',todayDate.strftime("%j"),'At',todayDate.strftime("%X"))
print('\nYou Entered', income, 'For Income')
print('You Entered', expense, 'For Expenses')
print('You Entered', miles, 'For Miles', '\nWith An Average Cost of: $', milesCostRound)
print('You Entered', hoursWorked, 'For Hours Worked')


print('\nYou made $',incomeRound, '\nWhile Spending: $',expenseRound, '\nYou drove ', miles, 'miles. ')
print('\nYour Averages Are:',  '\nHourly: $', hourlyRound, '\nWage Per Mile Driven: ', milesRound,'\n')

if goalReached < 0:
    print('You were: $',goalReached,'Short of your Goal Buster')
elif goalReached > 0:
    print('You Exceeded your goal by: $',goalReached)

#if statment - Did you reach your goal?
if income < dailyGoal:
    print('You Need To Grind Harder')
elif income > dailyGoal*2:
    print('Balling out of Control')
else:
    print('Good Job, Let Do Better Tommorow')

