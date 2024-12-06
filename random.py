# Dillon Matthews
# This program simulates a random walk in a lattice.

import turtle
from random import randint

walker = turtle.Turtle()
walker.speed(0)

walker.color("gray")
for i in range(-80, 90, 10):  
    walker.penup()
    walker.goto(-80, i)
    walker.pendown()
    walker.goto(80, i)
for i in range(-80, 90, 10):  
    walker.penup()
    walker.goto(i, -80)
    walker.pendown()
    walker.goto(i, 80)

walker.penup()
walker.goto(0, 0)
walker.pendown()
walker.pensize(2)
walker.color("black")
walker.speed(1)

while -80 <= walker.xcor() <= 80 and -80 <= walker.ycor() <= 80:
    direction = randint(0, 3)  # 0 = North, 1 = East, 2 = South, 3 = West
    if direction == 0:
        walker.setheading(90)  
    elif direction == 1:
        walker.setheading(0)   
    elif direction == 2:
        walker.setheading(270) 
    elif direction == 3:
        walker.setheading(180) 
    walker.forward(10)

turtle.done()
