import math #імпортуємо математику
import turtle as t #імпорт черепахи
import random


sndr = ['Ruslan Levchuk', 'Ukraine, Vinnytsia', 'Some street, 12/12', '21005']
rcpnt = ['Colin James Farrell', 'Ireland, Dublin', 'Another street, 24/42']
recipient_index = '704891'
#Розкоментувати, щоб було інтерактивним
"""
sender_nm, sender_country = input("Введіть ім'я відправника: "), input("Введіть країну, місто відправника: ")
sender_add, sender_index = input("Введіть вулицю та номер будинку відправника: "), input("Введіть індекс: ")
if not sender_index.isdigit() or len(sender_index)>6 or len(sender_index)<6:
    raise ValueError("Невірний індекс")
sndr = [sender_nm, sender_country, sender_add, sender_index]

recipient_nm, recipient_country = input("Введіть ім'я отримувача: "), input("Введіть країну, місто отримувача: ")
recipient_add, recipient_index = input("Введіть вулицю та номер будинку отримувача: "), input("Введіть індекс: ")
if not recipient_index.isdigit() or len(recipient_index)>6 or len(recipient_index)<6:
    raise ValueError("Невірний індекс")
rcpnt = [recipient_nm, recipient_country, recipient_add]
"""

t.speed(0)
t.setup(height=1000, width=2000)
#змінна, яка тримає поточну позицію курсора по Х
current_position_x = -500
current_position_y = -400

def paint_frame():
    t.pensize(width=2)
    t.up()
    t.setpos(-650, -460)
    t.down()
    t.left(90)
    t.forward(460*2)
    t.right(90)
    t.forward(640*2)
    t.right(90)
    t.forward(460*2)
    t.right(90)
    t.forward(640*2)
    t.up()

    t.setpos(-600, 350)
    t.left(180)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-600, 300)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-600, 250)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-600, 200)
    t.down()
    t.forward(600)
    t.up()

    t.setpos(-25, -50)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-25,-100)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-25, -150)
    t.down()
    t.forward(600)
    t.up()
    t.setpos(-25, -200)
    t.down()
    t.forward(600)
    t.up()

    paint_skeleton()

def paint_skeleton():
    t.pensize(width=1)
    t.up()
    t.setpos(-600, -280)
    def header():
        t.down()
        t.fillcolor('black')
        t.begin_fill()
        t.forward(50)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(15)
        t.end_fill()
        t.left(90)
        t.up()
        t.forward(100)
    def skeleton():
        def circ():
            t.fillcolor('grey')
            t.begin_fill()
            t.forward(5)
            t.down()
            t.circle(1)
            t.up()
            t.end_fill()

        for i in range(10):
            circ()
        t.left(90)
        for i in range(20):
            circ()
        t.left(90)
        for i in range(10):
            circ()
        t.left(90)
        for i in range(20):
            circ()
        t.left(135)
        for i in range(14):
            circ()
        t.left(135)
        for i in range(10):
            circ()
        t.right(135)
        for i in range(14):
            circ()
        t.right(135)
        t.forward(100)
        t.left(90)
        t.forward(51)



    for i in range(7):
        header()
    t.setpos(-500, -400)
    for i in range(6):
        skeleton()


def write_letter(recipient, sender, index):
    paint_frame()
    t.setpos(-600, 350)
    t.write('Кому: ', font='Waree')
    t.setpos(-490, 355)
    t.write(recipient[0], font='Z003')
    t.setpos(-600, 250)
    t.write('Куди: ', font='Waree')
    t.setpos(-490, 255)
    t.write(recipient[1], font='Z003')
    t.setpos(-575, 205)
    t.write(recipient[2], font='Z003')

    t.setpos(-25, -50)
    t.write('Від кого: ', font='Waree')
    t.setpos(140, -45)
    t.write(sender[0], font='Z003')
    t.setpos(-25, -150)
    t.write('Адреса: ', font='Waree')
    t.setpos(130, -145)
    t.write(sender[1], font='Z003')
    t.setpos(0, -195)
    t.write(sender[2]+', '+sender[3], font='Z003')

    t.setpos(current_position_x, current_position_y)
    write_index(index)

    ukraine_flag()

def random_color():
    t.pencolor((random.random(), random.random(), random.random()))

def next_number_position():

    global current_position_x
    current_position_x += 50
    t.setpos(current_position_x, current_position_y)

#оголошення функції для 1
def one():
    random_color()
    #змінну позиції треба зазначити як глобальну, шоб її
    #можна було міняти із функції
    global current_position_x
    # одразу додаємо 100, щоб наступна цифра чи пробіл почали малюватись
    # на 100 пунктів правіше. Це нам тре буде в кінці функції
    current_position_x += 50
    #підняли перо і перемістили вперед на 50
    t.up()
    t.forward(50)
    #опустили перо, провернули ліворуч на 90 град. і перемістили прямо на 100
    # це ми намалювали паличку одинички
    t.down()
    t.left(90)
    t.forward(100)
    #провернули перо на 135 град, щоб почати малювати стріху одинички
    t.left(135)
    #малюємо стріху одинички. використано модуль математики, щоб зробити чітку діагональ під кутом
    #45 град на ширину цифри. Це як гіпотенуза = корінь_кв(катет*2 + катет*2)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    #підінмаємо перу
    t.up()
    #провертаємо курсор на нульову позицію
    t.left(135)
    #виставляємо на позицію кінця цифри
    t.setpos(current_position_x, current_position_y)
    next_number_position()

def two():
    random_color()
    #змінну позиції треба зазначити як глобальну, шоб її
    #можна було міняти із функції
    global current_position_x
    # одразу додаємо 50, щоб перед перенесеням пера на наступну цифру воно знаходилось в нижньому правому кутку нашої цифри
    current_position_x += 50
    #перемістили вперед на 50 (щоб почати малювати двійку з нижньої лінії)
    t.forward(50)
    #опустили перо, провернули ліворуч на 180 град. і перемістили прямо на 50
    #намалювали нижню лінію двійки
    t.down()
    t.left(180)
    t.forward(50)
    #провернули перо направо на 135 град, щоб почати малювати гачок двійки
    t.right(135)
    #малюємо гачок двійки. використано модуль математики, щоб зробити чітку діагональ під кутом
    #45 град на ширину цифри. Це як гіпотенуза = корінь_кв(катет*2 + катет*2)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    #провертаємо курсор на 45 град вліво і малюємо паличку гачка двійки догори на 50
    t.left(45)
    t.forward(50)
    #провертаємо курсор на 90 і малюємо верхню лінію гачка одинички
    t.left(90)
    t.forward(50)
    #
    t.up()
    #провертаємо курсор на 0 позицію
    t.right(180)
    #виставляємо на позицію кінця цифри (нижній правий куток цифри) правому кутку нашої цифри
    t.setpos(current_position_x, 0)
    next_number_position()

def three():
    random_color()
    global current_position_x
    t.left(45)
    t.down()
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.forward(50)
    t.right(180)
    t.up()
    current_position_x += 50
    t.setpos(current_position_x, 0)
    next_number_position()

def four():
    random_color()
    global current_position_x
    t.forward(50)
    t.down()
    t.left(90)
    t.forward(100)
    t.up()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.up()
    current_position_x += 50
    t.setpos(current_position_x, 0)
    next_number_position()

def five():
    random_color()
    global current_position_x
    current_position_x += 50
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def six():
    random_color()
    global current_position_x
    current_position_x += 50
    t.left(90)
    t.forward(50)
    t.down()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.right(45)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def seven():
    random_color()
    global current_position_x
    current_position_x += 50
    t.down()
    t.left(90)
    t.forward(50)
    t.right(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.forward(50)
    t.right(180)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def eight():
    random_color()
    global current_position_x
    current_position_x += 50
    t.left(90)
    t.forward(50)
    t.right(90)
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def nine():
    random_color()
    global current_position_x
    current_position_x += 50
    t.down()
    t.left(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def zero():
    random_color()
    global current_position_x
    current_position_x += 50
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.up()
    t.setpos(current_position_x, 0)
    next_number_position()

def ukraine_flag():
    global current_position
    t.setpos(250, 300)
    t.fillcolor("yellow")
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.setpos(250, 250)
    t.fillcolor("blue")
    t.left(90)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.end_fill()
    t.up()

def write_index (index):
    t.pensize(width=10)
    for i in index:
        if i == '0':
            zero()
        elif i == '1':
            one()
        elif i == '2':
            two()
        elif i == '3':
            three()
        elif i == '4':
            four()
        elif i == '5':
            five()
        elif i == '6':
            six()
        elif i == '7':
            seven()
        elif i == '8':
            eight()
        elif i == '9':
            nine()

write_letter(rcpnt, sndr, recipient_index)

t.done()