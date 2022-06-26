import sys

expression = ''


def do(a, b, action, expression):

    if action == '-':
        res = a - b
        if res%1 == 0:
            res = int(res)
        return f"{expression}{res}"
    elif action == '+':
        res = a + b
        if res%1 == 0:
            res = int(res)
        return f"{expression}{res}"
    elif action == 'x':
        res = a * b
        if res%1 == 0:
            res = int(res)
        return f"{expression}{res}"
    elif action == '/':
        res = a / b
        if res%1 == 0:
            res = int(res)
        else:
            res = round(res, 2)
        return f"{expression}{res}"
    elif action == '^':
        res = a ** b
        if res % 1 == 0:
            res = int(res)
        else:
            res = round(res, 2)
        return f"{expression}{res}"

    else:
        return "Incorrect mathematical operation"



data = sys.argv

if data[1].isalpha():
    if data[1].lower() == 'help':
        print('Type data in format <NUMBER1> <NUMBER2> <ACTION>. Example: "5 1 -" means 5 - 1 = 4 ')
        print('Actions:  minus (-), plus (+), multiplication (x), division (/), power (^) ')
        print('key [-v] in the end - to print full mathematical expression')
        print('key [-f] in the end - to save data in file "result.txt"')
        quit()

if len(data) < 4:
    print('Three arguments must be given: two numbers and a mathematical operation')
    quit()
elif len(data) > 6:
    print('There are more of one optional argument')
    quit()

try:
    a = float(data[1])
    b = float(data[2])
    action = data[3]

    if len(data) == 5:
        if '-v' in data:
            expression = f"{data[1]} {data[3]} {data[2]} = "
        elif '-f' in data:
            file = open("result.txt", 'w')
            file.write(do(a, b, action, expression))
            file.close()
        else:
            print("incorrect optional argument")
            quit()
    elif len(data) == 6:
        if '-v' in data and '-f' in data:
            expression = f"{data[1]} {data[3]} {data[2]} = "
            file = open("result.txt", 'w')
            file.write(do(a, b, action, expression))
            file.close()

    print(do(a, b, action, expression))
    quit()
except ValueError:
    print("First and second arguments must contain numbers only!")
    quit()