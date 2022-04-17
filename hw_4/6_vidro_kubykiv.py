import random
def vidro_kubykiv(n=6,k=1):
    drops = []
    if k == 1:
        return random.randint(1, n)
    else:
        for i in range(k):
            drops.append(random.randint(1, n))
        return drops

print(f"Typical result: {vidro_kubykiv()}")
while 1:
    sides = int(input("Input number of sides "))
    drops = int(input("Input number of drops "))
    result = vidro_kubykiv(sides, drops)
    if type(result) is list:
        print(f"Result: {', '.join(str(i) for i in result)}")
    else:
        print(result)