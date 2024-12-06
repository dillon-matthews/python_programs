# Dillon Matthews
# This program calculates the total cost of purchasing baseballs.

baseballs = input("Enter the number of baseballs purchased: ")
baseballs = eval(baseballs)

cost_per_baseball = input("Enter the cost of each baseball: ")
cost_per_baseball = eval(cost_per_baseball)

total_cost = baseballs * cost_per_baseball

print("The total amount spent is:", total_cost)
