import pet
steps = int(input("Скільки кроків зробити?"))
direction = input("В яку сторону? (v - вперед / n - назад): ")

for i in range(steps):
    if direction == 'v':
        pet.vpered(steps)
        pet.golos(steps)
    elif direction == 'n':
        pet.nazad(steps)
        pet.golos(steps)