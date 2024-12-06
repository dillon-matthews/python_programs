print("Enter today's sales for five stores:")

sales = []
for i in range(1, 6):
    store_sales = int(input(f"Enter today's sales for store {i}: "))
    sales.append(store_sales)

print("\nSALES BAR CHART")
print("(Each * = $1000)")

for i in range(5):
    bar = sales[i] // 1000
    print(f"Store {i + 1}: {'*' * bar}")
