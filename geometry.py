# Dillon Matthews
# This program is a geometry calculator that calculates the area of a circle, rectangle, or triangle.

import math

def geometry_calculator():
    while True:
        # Display the menu
        print("\nGeometry Calculator")
        print("1. Calculate the Area of a Circle")
        print("2. Calculate the Area of a Rectangle")
        print("3. Calculate the Area of a Triangle")
        print("4. Quit")

        # Get the user's choice
        choice = int(input("Enter your choice (1-4): "))

        # Handle each choice
        if choice == 1:
            # Calculate the area of a circle
            radius = float(input("Enter the radius of the circle: "))
            if radius < 0:
                print("Error: Radius cannot be negative.")
            else:
                area = math.pi * radius ** 2
                print(f"The area of the circle is: {area:.2f}")
        elif choice == 2:
            # Calculate the area of a rectangle
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            if length < 0 or width < 0:
                print("Error: Length and width cannot be negative.")
            else:
                area = length * width
                print(f"The area of the rectangle is: {area:.2f}")
        elif choice == 3:
            # Calculate the area of a triangle
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            if base < 0 or height < 0:
                print("Error: Base and height cannot be negative.")
            else:
                area = 0.5 * base * height
                print(f"The area of the triangle is: {area:.2f}")
        elif choice == 4:
            # Quit the program
            print("Goodbye!")
            break
        else:
            # Invalid choice
            print("Error: Please enter a valid choice (1-4).")

# Run the calculator
geometry_calculator()
