
import turtle


def rectangle(color, l, b):

    myflag.begin_fill()
    myflag.fillcolor(color)
    myflag.speed(0)
    for i in range(2):
        myflag.forward(l)
        myflag.right(90)
        myflag.forward(b)
        myflag.right(90)
    myflag.end_fill()


def star(color, size):
    myflag.fillcolor(color)
    myflag.begin_fill()
    myflag.color(color)
    myflag.setheading(90)
    for i in range(5):
        myflag.left(70)
        myflag.forward(size)
        myflag.right(144)
        myflag.forward(size)

    myflag.end_fill()


myflag = turtle.Turtle()


myflag.width(3)
myflag.up()
myflag.goto(0, -300)
myflag.down()
myflag.goto(0, 300)
myflag.width(1)
rectangle('white', 300, 195)

#  Drawing 7 red rectangles
inc = 300
for i in range(7):
    rectangle('#BF0A30', 300, 15)
    inc = inc - 30
    myflag.goto(0, inc)


# Drawing the blue square
myflag.goto(0, 300)
rectangle("#3c3b6e", 150, 105)

# Tricky stars

loop1 = 305
loop2 = 290

for outerloop in range(5):
    x = 10
    loop1 = loop1 - 10

    for i in range(6):
        myflag.up()
        myflag.goto(x, loop1-10)
        myflag.down()
        star('white', 3)
        x = x+25

    if outerloop != 4:
        myflag.up()
        y = 10
        for i in range(5):
            myflag.up()
            myflag.goto(y+12, loop1-20)
            myflag.down()
            star('white', 3)
            y = y+25
        loop1 = loop1 - 11
    else:
        myflag.up()
        myflag.goto(0, -300)
        break

input()
