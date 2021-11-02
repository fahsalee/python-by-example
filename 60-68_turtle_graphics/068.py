import turtle, random


turtle.Screen().bgcolor("black")
turtle.color("white")

lines = random.randint(10, 20)

for line in range(lines):
    turtle.right(random.randint(20, 170))
    turtle.forward(random.randint(50, 120))

turtle.exitonclick()