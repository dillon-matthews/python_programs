# Dillon Matthews
# This program draws a clock showing the time 9:20:50.

import turtle

# turtle objects for the clock
clock = turtle.Turtle()
clock.speed(0)

# clock face
clock.penup()
clock.goto(0, -200)
clock.pendown()
clock.circle(200)

# clock numbers
clock.penup()
positions = [(0, 165, '12'), (185, 0, '3'), (0, -185, '6'), (-195, 0, '9')]
for x, y, num in positions:
    clock.goto(x, y)
    clock.write(num, align="center", font=("Arial", 16, "normal"))

# clock hands
def draw_hand(length, angle, color):
    clock.penup()
    clock.goto(0, 0)
    clock.setheading(angle)
    clock.pendown()
    clock.color(color)
    clock.forward(length)
    clock.penup()
    clock.goto(0, 0)

draw_hand(120, 90, "black")   
draw_hand(150, 60, "blue")    
draw_hand(170, 50, "red")     

turtle.done()
