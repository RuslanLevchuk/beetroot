set_1 = {1, 5, 7, 9}
set_2 = {5, 6, 8, 1}
set_3 = set()

for i in set_1:
    if i in set_2:
        pass
    else:
        set_3.add(i)
for i in set_2:
    if i in set_1:
        pass
    else:
        set_3.add(i)
print(set_3)


A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
print(A.symmetric_difference(B))


