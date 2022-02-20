import random
def randomizer (symbol):
    value_1 = random.randint(1, 11)
    value_2 = random.randint(1, 11)
    if symbol == '+':
        result = value_1+value_2
    elif symbol == '-':
        result = value_1-value_2
    elif symbol == '*':
        result = value_1*value_2
    elif symbol == '/':
        result = value_1/value_2
    return value_1, value_2, result, symbol

print("Let see if you have basic knowledge in mathematics!\n Solve expressions below:")
operation = ['+', '-', '*', '/']
print(random.randint(0, 3))

while 1:
    a, b, res, symbol = randomizer(operation[random.randint(0, 3)])
    print(f"Type the result of expression {a} {symbol} {b} = ", end='')
    usr_result = input()
    try:
       usr_result= float(usr_result)
       if symbol == '/' and usr_result == round(res, 1):
           print("Right!")
       elif usr_result == res:
           print("Right!")
       else:
           if symbol == '/':
               print(f'Wrong! { round(res, 1)} is right answer.')
           else:
               print(f'Wrong! {res} is right answer.')

    except ValueError:
        if symbol == '/':
            print(f'Wrong! {round(res, 1)} is right answer.')
        else:
            print(f'Wrong! {res} is right answer.')