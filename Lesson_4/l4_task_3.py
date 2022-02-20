import random
#1 method
str = list(input("Type world: "))
for i in range(5):
    random.shuffle(str)
    print(''.join(str))

#2 method
str = list(input("Type world: "))
some_list = []
for i in range(5):
    while len(str) != len(some_list):
       index_val = random.randint(0, len(str)-1)
       if index_val not in some_list:
           some_list.append(index_val)

    for i in some_list:
        print(str[i], end='')
    print('')
    some_list = []


