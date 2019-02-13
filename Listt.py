my_List = [1,2,3,4,5,6,7,8,9,['a','b','c']]

print(my_List[9][2])

my_Dict = {'key1':[1,2,3,4],'key2':['A','B','C','D'],'key4':{'key1':[1,2,3,4],'key2':['A','c','C','D']}}

print(my_Dict['key2'])

my_Dict['key1'] = 'New Item'

my_Dict2 = {'key1':'hello','Key2':'World'}

print(my_Dict2)

print(my_Dict2.items())


print(type(my_Dict2))

print(type(my_List))

tuples=(1,2,3)

print(tuples)

print(tuples.count(2))

print(tuples.index(3))