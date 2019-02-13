# d = {'a': 1, 'b': 2, 'c': 3}
#
# for item2, item1 in d.items():
#     print(item2, '=', item1)
#
# index = 0
# for letter in 'Fuck':
#     print('At index {} the letter is {}'.format(index,letter))
#     index += 1
#
#
# with open('text.txt', 'r+') as f:
#
#     exm=f.readlines()
#     print(exm)
# for i in exm[0:7]:
#     print(i)

my_list = [1, 2, 3, 4, 5]
my_list2 = [99, 88, 77, 66, 55, 99, 999, 888, 555, 588]

my_lists = ' '.join(str(i) for i in my_list)

print(my_lists)