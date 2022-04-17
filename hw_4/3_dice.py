import random
def dice():
    return random.randint(1, 6)

while 1:
    inp = input('Press ENTER to make drop (any other key will raise exit): ')
    if inp == '':
        print(dice())
    else:
        break
