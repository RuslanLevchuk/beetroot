list_1 = list(range(1, 101))
print(list_1)
i = 0 #for looping

# without while loop
list_2 = list(x for x in list_1 if x%7 == 0 and x%5 != 0)
print(list_2)

# with while loop
list_2 = []
while i<len(list_1):
    if list_1[i]%7 == 0 and list_1[i]%5 != 0:
        list_2.append(list_1[i])
    i += 1
