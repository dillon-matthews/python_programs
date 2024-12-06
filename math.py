import random

# Dillon Matthews
# This program serves as a math tutor for basic addition.

# Generate two random numbers between 1 and 9
num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

# Display the math problem
print(f"  {num1}")
print(f"+ {num2}")
print("-----")

# Ask the student for their answer
student_answer = int(input("Enter your answer: "))

# Calculate the correct answer
correct_answer = num1 + num2

# Check if the student's answer is correct
if student_answer == correct_answer:
    print("Congratulations! You are correct.")
else:
    print(f"Sorry, the correct answer is {correct_answer}.")
