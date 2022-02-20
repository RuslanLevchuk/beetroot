str = input('Введіть рядок: ')
numbs = 0
signs = 0

for i in str:
    if i.isdigit():
        numbs += 1
    elif i.isalpha():
        signs += 1
print(f"Кількість цифр: {numbs}")
print(f"Кількість літер: {signs}")
