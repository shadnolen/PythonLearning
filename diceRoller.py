import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
total = die1 + die2
count = 0


while total != 7:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1 + die2
    print(die1, die2, '= ', die1 + die2, end=' ')   
    count = count + 1

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
else:
    
    print('You rolled:', count, 'Times')
    if count == 0:
        print('No Roll, Dice Out Reroll')
    if count ==1:
        print('Winner, Winner Chicken Dinner')
    else:
        print("Place your  bets boys and girls")