file = open('fio.txt', 'r')
name = file.readline().strip()
date = file.readline().split('.')
file.close()
print(f'Hi, {name}! Your age is {2022 - int(date[0])}')

