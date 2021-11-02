import turtle


def draw_square(colour):
    turtle.fillcolor(colour)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(80)
        turtle.right(90)
    turtle.end_fill()


def make_gap():
    turtle.penup()
    turtle.forward(100)


turtle.Screen().bgcolor("black")
turtle.color("white")

draw_square("blue")
make_gap()

draw_square("purple")
make_gap()

draw_square("red")

turtle.exitonclick()