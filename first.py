import itertools, random, datetime

# Print Test  
txt = 'best things in life are free'
print(txt.title())

# Date 
todayDate = datetime.datetime.now()
print(todayDate.strftime("%X"), end=' ')
print(todayDate.strftime("%A"),"- ", end='')
print(todayDate.day, '- ', end='') 
print(todayDate.strftime("%y"))
print('Day ', todayDate.strftime("%j"), ' of The Year')

#Find Gravity 
Gravity = 6.673e-11
Mass = 5.98e24
distance_to_center = 6.38e6
accel_gravity = (Gravity * Mass) / (distance_to_center ** 2)
print(accel_gravity)

# Dictionary Basics
carMakers= {'Acura': 'Japan', 'Fiat': 'Egypt'}
carMakers['Fiat'] = 'Italy'
carMakers['Tesla'] = 'USA'

print('Acura is made in', carMakers['Acura'])
print('Fiat is made in', carMakers['Fiat'])
print('Tesla is made in', carMakers['Tesla'])

# If-Else



