letter = ['A', 'B', 'C', 'a', 'b', 'c']

Number = [1, 2, 3, 0]

pos=-1

query = input("Enter your Query whether it's a number or not: ")

for x in range(len(Number)):
    if query == str(Number[x]):
        pos=x+1
        print('This is the Number and The Position is {}'.format(pos))


for x in range(len(letter)):
    if query == letter[x]:
        pos=x+1
        print('This is the Alphabet and The Position is {}'.format(pos))
if pos == -1:
    print('Not Found')

