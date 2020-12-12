import random, itertools

deck = list(itertools.product(range(1, 14), ['Clubs', 'Hearts', 'Diamonds', 'Spades']))


random.shuffle(deck)


print('Cards: ')

for i in range(52):

    if deck[i][0] == 1:
        print("Ace", 'Of', deck[i][1])
    if deck[i][0] == 11:
        print("Jack", 'Of', deck[i][1])
    if deck[i][0] == 12:
        print("Queen", 'Of', deck[i][1])
    if deck[i][0] == 13:
        print("King", 'Of', deck[i][1])  
    else: 
        print(deck[i][0], 'Of', deck[i][1])


   