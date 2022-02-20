import random
list_1 = []
list_2 = []
list_len = 10
max_range = 10

while len(list_1) < list_len:
    list_1.append(random.randint(1, max_range))
    list_2.append(random.randint(1, max_range))

print(f"First random list: {list_1}")
print(f"Second random list: {list_2}")

print(f"Unique elements in both lists via symmetric_defference: {list(set(list_1).symmetric_difference(set(list_2)))}")

print(f"Unique elements in both lists via XOR operator: {list(set(list_1) ^ set(list_2))}")

