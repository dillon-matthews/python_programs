# Dillon Matthews
# This program displays the day of the week based on a number from 1 to 7.

# Ask the user for a number
number = int(input("Enter a number (1-7): "))

# Check the number and display the corresponding day of the week
if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif number == 3:
    print("Wednesday")
elif number == 4:
    print("Thursday")
elif number == 5:
    print("Friday")
elif number == 6:
    print("Saturday")
elif number == 7:
    print("Sunday")
else:
    print("Error: Number must be between 1 and 7.")
