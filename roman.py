# Dillon Matthews
# This program converts a number between 1 and 10 to its Roman numeral equivalent.

# Prompt the user to enter a number
number = int(input("Enter a number between 1 and 10: "))

# Validate the input and display the corresponding Roman numeral
if number < 1 or number > 10:
    print("Error: Please enter a number between 1 and 10.")
else:
    if number == 1:
        print("Roman numeral: I")
    elif number == 2:
        print("Roman numeral: II")
    elif number == 3:
        print("Roman numeral: III")
    elif number == 4:
        print("Roman numeral: IV")
    elif number == 5:
        print("Roman numeral: V")
    elif number == 6:
        print("Roman numeral: VI")
    elif number == 7:
        print("Roman numeral: VII")
    elif number == 8:
        print("Roman numeral: VIII")
    elif number == 9:
        print("Roman numeral: IX")
    elif number == 10:
        print("Roman numeral: X")
