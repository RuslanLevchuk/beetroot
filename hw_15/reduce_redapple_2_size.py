import os
file = open('red_apple_2.log', 'r')
lines = (file.readlines())
file.close()

file_2 = open('new_red_apple.log', 'a+')
file_2.close()

while os.path.getsize('new_red_apple.log') <= 100000000:
    file_2 = open('new_red_apple.log', 'a+')
    file_2.write(lines.pop(0))
    file_2.close()