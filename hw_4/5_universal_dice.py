import random
def universal_dice(sides=6):
    return random.randint(1, sides)

while 1:
    inp = input('Press ENTER to make drop of 6-side dice (any other key = break): ')
    if inp == '':
        print(universal_dice())
    else:
        break

num = int(input('Press number of sides of dice: '))
while 1:
    inp = input(f'Press ENTER to make drop of {num}-side dice (any other key = break: ')
    if inp == '':
        print(universal_dice(num))
    else:
        break
