# Dillon Matthews
# This program guesses the user's birthday based on their answers.

# Define the sets
SET1 = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31}
SET2 = {2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31}
SET3 = {4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31}
SET4 = {8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31}
SET5 = {16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}

# Initialize day
day = 0

# Ask the user if their birthday is in each set
if int(input(f"Is your birthday in SET1 {SET1}? Enter 0 for No and 1 for Yes: ")) == 1:
    day += 1  
if int(input(f"Is your birthday in SET2 {SET2}? Enter 0 for No and 1 for Yes: ")) == 1:
    day += 2  
if int(input(f"Is your birthday in SET3 {SET3}? Enter 0 for No and 1 for Yes: ")) == 1:
    day += 4  
if int(input(f"Is your birthday in SET4 {SET4}? Enter 0 for No and 1 for Yes: ")) == 1:
    day += 8  
if int(input(f"Is your birthday in SET5 {SET5}? Enter 0 for No and 1 for Yes: ")) == 1:
    day += 16  

# Display the birthday
print(f"Your birthday is on the {day}.")
