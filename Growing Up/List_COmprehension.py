import random

Lis_d = "Secret Agents are super cool Savage"

for S_words in Lis_d.split():
    if len(S_words)%2==0:
        print(S_words)

print(list(range(0,11,2)))


empty_list = []

for num in range(0,10):
    empty_list.append(random.randint(0,100))
print(empty_list)