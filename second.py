
words = input('Enter Text Yo: ')
print(words)
words = words.split(' ')

for i in words:
    if len(i) >= 3:
        i = i + "%say" % (i[0])
        i = i[1:]
        print(i)
else:


    REFRAIN = '''
%d  bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 99
bottles = bottles_of_beer
while bottles_of_beer > 1:
    print (REFRAIN % (bottles_of_beer, bottles,
        bottles_of_beer - 1))
    bottles_of_beer -= 1
    bottles -= 2

if bottles_of_beer == 0:
    print('You Drunk?')
    