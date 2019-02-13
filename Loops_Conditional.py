a=int(input('Please Enter The Query'))

if a==2:
    print('True')
elif a>2:
    print('A is greater')
elif a<2:
    print('A is less Than')
else:
    print('False')


print('Welcome Agent')

passcode=1

while passcode != 123:
    print('Please Provide your passcode')
    passcode = int(input())
    if passcode ==123:
        print('\tAccess Granted')


