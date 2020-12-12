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
year = random.randint(1000, 2200)
if year > 2101:
    print(year, end=' ')
    print('Distant Future')   
elif year > 2000:
    print(year, end=' ')
    print('20th Centry Fox')
elif year < 1900:
    print(year, end=' ')
    print('Now thats some old ass Sh@t')

#Dice try

die1 = random.randint(1,6)
die2 = random.randint(1,6)




    
print(die1, die2 , '= ', die1 + die2, end=' ')
 
    #Craps
if die1 + die2 == 2:
    print('Snake Eyes')
elif die1 + die2 == 3:
    print('3 Craps')
elif die1 + die2 == 11:
    print('Yo, Ho, Ho Elevon')
   #Doubles
elif die1 == 2 and die2 == 2:
    print('Two, Two Like a Choo, Choo')
elif die1 == 3 and die2 == 3:
    print('Rainbow')
elif die1 == 4 and die2 == 4:
    print('Fo, Fo on da Floor')
elif die1 == 5 and die2 == 5:
    print('Hard Ten, A girls best friend')
elif die1 == 6 and die2 == 6:
    print('Get your fix on route 66')
    #Singles
elif die1 + die2 == 4:
    print('Four is a bore')  
elif die1 + die2 == 5:
    print('Five on the black hand side') 
elif die1 + die2 == 6:
    print('Get yo fix wit da Six')    
elif die1 + die2 == 8:
    print('Eight skate and make the casino donate')
elif die1 + die2 == 9:
    print('Nine is fine ')
elif die1 + die2 == 10:
    print('Dime bizag ')
    #Out
elif die1 + die2 == 7:
   print('Seven Out')

total = 0
total = die1 + die2 
print(total, end='')
if(total % 2) ==0:
    print(" Even Steven ")
else:
    print(" Odd Todd ")
if total > 1:
    for i in range(2, total):
        if(total % i) == 0:
            print(total, 'Not so Prime')
            print(i, 'times', total//i, 'is', total)
            break
    else:
        print(total, ' Is Prime')

print()

