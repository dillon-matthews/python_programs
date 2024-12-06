# Dillon Matthews
# This program calculates the total amount earned from candy bar sales.

candy_bars_sold = input("Enter the number of candy bars sold: ")
candy_bars_sold = eval(candy_bars_sold)

cost_per_bar = input("Enter the cost paid for each candy bar: ")
cost_per_bar = eval(cost_per_bar)

selling_price_per_bar = input("Enter the selling price for each candy bar: ")
selling_price_per_bar = eval(selling_price_per_bar)

total_earned = candy_bars_sold * (selling_price_per_bar - cost_per_bar)

print("The total amount earned is:", total_earned)
