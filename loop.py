# Dillon Matthews
# This program calculates the sum of numbers entered by the user using a loop.

total = 0
sentinel = -1

print("Enter numbers to sum them. Enter -1 to stop.")

while True:
    number = int(input("Enter a number (-1 to stop): "))
    if number == sentinel:
        break
    total += number

print("The total sum is:", total)
