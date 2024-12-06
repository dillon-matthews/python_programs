# Dillon Matthews
# This program uses the turtle library to draw a star.

import turtle

# turtle object
star_drawer = turtle.Turtle()

# turtle speed
star_drawer.speed(5)

# Draw the star
for _ in range(5):
    star_drawer.forward(100)  # forward by 100 pixels
    star_drawer.right(144)  # 144 degrees to form a star

turtle.done()
