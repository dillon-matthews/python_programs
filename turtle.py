# Dillon Matthews
# This program uses the turtle library to draw a circle, a square, and write text to the screen.

import turtle

# Name the turtle by creating a turtle object
my_turtle = turtle.Turtle()

# Change the shape of the turtle (arrow)
my_turtle.shape("arrow")

# Move the turtle to 100, 100 (without drawing a line)
my_turtle.penup()
my_turtle.goto(100, 100)

# Draw a red circle with a radius of 50 (fill color is red)
my_turtle.pendown()
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.circle(50)
my_turtle.end_fill()

# Move the turtle to 200, 100 (without drawing a line)
my_turtle.penup()
my_turtle.goto(200, 100)

# Draw a square with sides equal to 75 pixels, each side a different color
my_turtle.pendown()
side_colors = ["blue", "green", "yellow", "purple"]
for color in side_colors:
    my_turtle.pencolor(color)
    my_turtle.forward(75)
    my_turtle.right(90)

# Move the turtle to the center of the screen (without drawing a line)
my_turtle.penup()
my_turtle.goto(0, 0)

# Write "Having Fun!!!" in blue, font size 40
my_turtle.pencolor("blue")
my_turtle.write("Having Fun!!!", align="center", font=("Arial", 40, "bold"))

# End the program
turtle.done()
