import dicer as d
print(d.dice())
print(d.graph_dice())

#universal dice
u_d = d.universal_dice(int(input('Press number of sides of dice: ')))
print(u_d)

#vidro
sides = int(input("Input number of sides "))
drops = int(input("Input number of drops "))
result = d.vidro_kubykiv(sides, drops)
if type(result) is list:
    print(f"Result: {', '.join(str(i) for i in result)}")
else:
    print(result)

