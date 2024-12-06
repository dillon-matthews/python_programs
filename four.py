# Dillon Matthews
# This program uses the turtle library to draw four circles in the center of the screen.

import turtle

# Create a turtle object
george = turtle.Turtle()

# Set up the turtle speed
george.speed(5)

# Draw the first circle
george.penup()
george.goto(0, 50)  # top circle
george.pendown()
george.circle(50)

# Draw the second circle
george.penup()
george.goto(0, -50)  # bottom circle
george.pendown()
george.circle(50)

# Draw the third circle
george.penup()
george.goto(-50, 0)  # left circle
george.pendown()
george.circle(50)

# Draw the fourth circle
george.penup()
george.goto(50, 0)  # right circle
george.pendown()
george.circle(50)

# End the turtle program
turtle.done()
