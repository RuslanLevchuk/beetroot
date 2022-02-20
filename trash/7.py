"""Write a Python program to convert temperatures to and from celsius, Fahrenheit.
Formula : c/5 = f-32/9
[ where c = temperature in celsius and f = temperature in Fahrenheit"""

inp = input('Input temperature in format f** or c**: ')
inp.lower()
if 'f' in inp:
    temp_type = 'f'
    inp = inp.replace('f', '')
elif 'c' in inp:
    temp_type = 'c'
    inp = inp.replace('c', '')
else:
    print('Wrong format')

print(inp)


if inp.find('.'):
    val_type = 'float'
    spliter = '.'
elif inp.find(','):
    val_type = 'float'
    spliter = ','
else:
    val_type = 'int'

if val_type == 'float':
    values = inp.split(spliter)
else:
    values = inp

print(values)


"""
if ',' and '.' in inp:
   val_type = 'float'
else:
    val_type = 'int'
temp_value = 0
print(val_type)
values = inp.split()
for i in inp:
    if i.isalpha():
        temp_type = i
    elif i.isdigit():
        pass

"""