#Task_1
name = 'ruslan'
day = 'saturday'
name = name.capitalize()
day = day.capitalize()
greeting_string = 'Good day {}! {} is a perfect day to learn some python.'
print(f"Good day {name}! {day} is a perfect day to learn some python.")
print('Good day {0}! {1} is a perfect day to learn some python.'.format(name, day))
print(greeting_string.format(name, day))
print('Good day %s! %s is a perfect day to learn some python.\n' %(name, day))

#Task_2
first_nm = 'Ruslan'
last_nm = 'Levchuk'
full_nm = first_nm + ' ' + last_nm
print(f'Hey you {full_nm}! Welcome in Python world!')
full_nm = ' '.join([first_nm, last_nm])
print(f'Hi {full_nm}! You look like Brad Pitt!\n')

#Task_3
var_1 = 20
var_2 = 6
print(f'Addition: {var_1} + {var_2} = {var_1+var_2}')
print(f'Subtraction: {var_1} - {var_2} = {var_1-var_2}')
print(f'Division: {var_1} / {var_2} = {var_1/var_2:.2f}')
print(f'Multiplication:  {var_1} * {var_2} = {(var_1*var_2)}')
print(f'Exponent (Power): {var_1}^{var_2} = {var_1**var_2}')
print(f'Modulus: {var_1} % {var_2} = {var_1%var_2}')
print(f'Floor division: {var_1} // {var_2} = {var_1//var_2}')
