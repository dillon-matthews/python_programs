# Kilometer Converter
def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

kilometers = float(input("Enter distance in kilometers: "))
miles = kilometers_to_miles(kilometers)
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

# Paint Job Estimator
def paint_job_estimator(square_feet, paint_price_per_gallon):
    gallons_of_paint = square_feet / 112
    hours_of_labor = gallons_of_paint * 8
    paint_cost = gallons_of_paint * paint_price_per_gallon
    labor_charges = hours_of_labor * 35.0
    total_cost = paint_cost + labor_charges
    return {
        "gallons_of_paint": round(gallons_of_paint),
        "hours_of_labor": round(hours_of_labor, 2),
        "paint_cost": round(paint_cost, 2),
        "labor_charges": round(labor_charges, 2),
        "total_cost": round(total_cost, 2)
    }

square_feet = float(input("Enter the square feet of wall space to be painted: "))
paint_price_per_gallon = float(input("Enter the price of the paint per gallon: "))

estimation = paint_job_estimator(square_feet, paint_price_per_gallon)

print(f"Gallons of paint required: {estimation['gallons_of_paint']}")
print(f"Hours of labor required: {estimation['hours_of_labor']} hours")
print(f"Cost of the paint: ${estimation['paint_cost']:.2f}")
print(f"Labor charges: ${estimation['labor_charges']:.2f}")
print(f"Total cost of the paint job: ${estimation['total_cost']:.2f}")

# Falling Distance
def falling_distance(time):
    g = 9.8
    return 0.5 * g * time ** 2

for t in range(1, 11):
    distance = falling_distance(t)
    print(f"Time: {t} seconds, Falling Distance: {distance:.2f} meters")

# Prime Numbers
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Prime Number List
print("Prime numbers from 1 to 100:")
for n in range(1, 101):
    if is_prime(n):
        print(n, end=" ")

# Random Number Guessing Game
import random

def guessing_game():
    while True:
        random_number = random.randint(1, 100)
        print("I have generated a random number between 1 and 100.")
        guess_count = 0
        while True:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            if guess > random_number:
                print("Too high, try again.")
            elif guess < random_number:
                print("Too low, try again.")
            else:
                print(f"Congratulations! You guessed the number in {guess_count} tries.")
                break
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

guessing_game()

# Turtle Graphics: Modular Snowman
import turtle

def drawBase():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.circle(100)

def drawMidSection():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(75)

def drawHead():
    turtle.penup()
    turtle.goto(0, 80)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.goto(-15, 130)
    turtle.pendown()
    turtle.dot(10)  
    turtle.penup()
    turtle.goto(15, 130)
    turtle.pendown()
    turtle.dot(10)  
    turtle.penup()
    turtle.goto(0, 110)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(15, 180)  

def drawArms():
    turtle.penup()
    turtle.goto(-75, 20)
    turtle.pendown()
    turtle.goto(-150, 80)  
    turtle.penup()
    turtle.goto(75, 20)
    turtle.pendown()
    turtle.goto(150, 80)  

def drawHat():
    turtle.penup()
    turtle.goto(-50, 180)
    turtle.pendown()
    turtle.setheading(0)
    turtle.fillcolor("black")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-30, 200)
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(90)
    turtle.end_fill()

def main():
    turtle.speed(3)
    drawBase()
    drawMidSection()
    drawHead()
    drawArms()
    drawHat()
    turtle.done()

main()
