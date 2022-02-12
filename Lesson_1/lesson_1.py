#Task_2:
a = 'Beetroot'
b = 'is'
c = 'awesome'
d = '!'
e = 'vika'
f = 'is'
g = 'a'
h = 'wonderful'
i = 'teacher'

#Separator example
print(a.upper(), b.upper(), c.upper(), d.upper(), sep=' |-|-| ')

#End example
print(e.capitalize(), f, g, h, i, end=' :D\n')
str1 = a + ' ' + b + ' ' + c
str2 = e + ' ' + f + ' ' + g + ' ' + h + ' ' + i

#Both parameters example
print(str1, str2, sep='_and_', end='. Yes she is!\n')

#Task_2:
symbol = '#'

#Hell yeah method
def print_oh(smbl):
    if len(symbol) != 1:
        print('Variable must have only one symbol!')
        return
    for row in range(11):
        for col in range(9):
            if row == 0 or row == 4 or row == 8:
                print(smbl, end='')
                if col == 8:
                    print('')
            elif row == 1 or row == 2 or row == 3 or row == 6 or row == 7 or row == 9 or row == 10:
                if col == 0 or col == 8:
                    print(smbl, end='')
                    if col == 8:
                        print('')
                else:
                    print(' ', end='')
            elif row == 5 and col == 1:
                print('')
    print('')

print_oh(symbol)

#Just method
print(9*symbol+'\n'+symbol+'\t\t'+symbol+'\n'+symbol+'\t\t'+symbol+'\n'+symbol+'\t\t'+symbol+'\n'+9*symbol, end='\n\n')
print(symbol+'\t\t'+symbol+'\n'+symbol+'\t\t'+symbol+'\n'+9*symbol+'\n'+symbol+'\t\t'+symbol+'\n'+symbol+'\t\t'+symbol+'\n')


