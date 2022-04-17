import random
def dice():
    value = random.randint(1, 6)
    if value == 1:
        return '⚀'
    elif value == 2:
        return '⚁'
    elif value == 3:
        return '⚂'
    elif value == 4:
        return '⚃'
    elif value == 5:
        return '⚄'
    else:
        return '⚅'


while 1:
    inp = input('Press ENTER to make drop (any other key will raise exit): ')
    if inp == '':
        print(dice())
    else:
        break