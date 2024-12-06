# Lottery Number Generator
import random

lottery_numbers = [random.randint(0, 9) for _ in range(7)]
print("Lottery Numbers:", lottery_numbers)

# Number Analysis Program
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(20)]
print("Lowest number:", min(numbers))
print("Highest number:", max(numbers))
print("Total of numbers:", sum(numbers))
print("Average of numbers:", sum(numbers) / len(numbers))

# Population Data
with open('USPopulation.txt', 'r') as file:
    populations = [int(line.strip()) for line in file]

population_changes = [populations[i+1] - populations[i] for i in range(len(populations) - 1)]
average_change = sum(population_changes) / len(population_changes)
greatest_increase = max(population_changes)
smallest_increase = min(population_changes)
year_greatest_increase = 1950 + population_changes.index(greatest_increase) + 1
year_smallest_increase = 1950 + population_changes.index(smallest_increase) + 1

print("Average annual change in population:", average_change)
print("Year with greatest increase in population:", year_greatest_increase)
print("Year with smallest increase in population:", year_smallest_increase)

# Prime Number Generation
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

user_input = int(input("Enter an integer greater than 1: "))
numbers = list(range(2, user_input + 1))

for num in numbers:
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is a composite number.")
