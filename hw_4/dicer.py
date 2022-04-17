import random
def dice():
    return random.randint(1, 6)

def graph_dice():
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

def universal_dice(sides=6):
    return random.randint(1, sides)

def vidro_kubykiv(n=6,k=1):
    drops = []
    if k == 1:
        return random.randint(1, n)
    else:
        for i in range(k):
            drops.append(random.randint(1, n))
        return drops