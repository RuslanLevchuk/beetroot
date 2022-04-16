f = open('white_house_2017_salaries_com.csv', 'r', encoding='utf-8')
headers = f.readline().split(';')
f.close()
info = {}
while True:
    for n in headers:
        info[n.strip()] = input(f"Input your {n.strip()}: ")


    f = open('white_house_2017_salaries_com.csv', 'a', encoding='utf-8')
    line = ''
    for n in headers:
        line += (info[n.strip()])
        if n != 'POSITION TITLE\n':
            line += ';'
        else:
            line += '\n'
    f.write(line)
    f.close()
    line = ''
    print('Another One... ')
