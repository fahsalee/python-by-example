import turtle
#import random

turtle.Screen().bgcolor("black")
turtle.color("white")

#colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for shape in range(10):
    turtle.right(36)
    for side in range(8):
#        turtle.color(random.choice(colours))
        turtle.forward(100)
        turtle.right(45)

turtle.exitonclick()