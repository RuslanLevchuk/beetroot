import math
def sqare(a):
    return (a*4, a*a, round(math.sqrt(a**2 + a**2), 2))

value = int(input("Введіть сторону квадрата: "))

per, sq, dia = sqare(value)
print(f"Периметр {per} м\nПлоща {sq} кв. м.\nДіагональ {dia} м")