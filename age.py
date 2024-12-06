# Dillon Matthews
# This program classifies a person's age as infant, child, teenager, or adult.

# Ask the user to enter a person's age
age = int(input("Enter the person's age: "))

# Determine the age classification
if age <= 1:
    print("This person is an infant.")
elif age > 1 and age < 13:
    print("This person is a child.")
elif age >= 13 and age < 20:
    print("This person is a teenager.")
else:
    print("This person is an adult.")
