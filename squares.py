import turtle

t = turtle.Turtle()
t.speed(0)

for i in range(100):
    for _ in range(4):
        t.forward(10 + i * 5)
        t.left(90)
    t.penup()
    t.goto(-i * 2.5, -i * 2.5)
    t.pendown()

turtle.done()
