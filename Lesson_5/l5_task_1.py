import random
list_1 = []

while len(list_1) < 10:
    list_1.append(random.randint(0, 128))

print(f"Random list is {list_1}\n"
      f"And its maximum number is {max(list_1)}")