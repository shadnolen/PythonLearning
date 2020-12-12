import random, itertools

deck = list(itertools.product(range(1, 14), ['Clubs', 'Hearts', 'Diamonds', 'Spades']))

random.shuffle(deck)

print('Cards: ')
for i in range(2):
    print(deck[i][0], 'Of', deck[i][1])


   