import math
import turtle as t
current_position = -300
def one():
    t.pencolor((0.2, 0.8, 0.55))
    global current_position
    current_position += 50
    t.up()
    t.forward(50)
    t.down()
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.up()
    t.setpos(current_position, 0)
    t.left(135)


def two():
    t.pensize(width=5)
    global current_position
    current_position += 50
    t.up()
    t.forward(50)
    t.down()
    t.backward(50)
    t.left(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.up()
    t.setpos(current_position, 0)
    t.left(180)




t.up()
t.setpos(current_position, 0)
one()
two()


t.done()





