import turtle

def draw_bar_chart(sales):
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    for sale in sales:
        height = sale / 100
        turtle.fillcolor("blue")
        turtle.begin_fill()
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

def draw_line_chart(sales):
    turtle.penup()
    turtle.goto(-180, sales[0] / 100)
    turtle.pendown()
    for i, sale in enumerate(sales):
        turtle.goto(-180 + i * 50, sale / 100)

sales = []
for i in range(1, 6):
    sale = int(input(f"Enter today's sales for store {i}: "))
    sales.append(sale)

draw_bar_chart(sales)
turtle.reset()
draw_line_chart(sales)
turtle.done()
