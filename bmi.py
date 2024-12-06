# Dillon Matthews
# This program calculates a person's BMI and displays their weight category.

def calculate_bmi():
    # Get the user's weight and height
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))

    # Validate input
    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive values.")
        return

    # Calculate BMI
    bmi = (weight * 703) / (height ** 2)

    # Display BMI
    print(f"Your BMI is: {bmi:.2f}")

    # Determine weight category
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi <= 25:
        print("You have an optimal weight.")
    else:
        print("You are overweight.")

# Run the BMI calculator
calculate_bmi()
