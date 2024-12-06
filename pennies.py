days = int(input("Enter the number of days worked: "))

while days < 1:
    print("The number of days must be at least 1.")
    days = int(input("Enter the number of days worked: "))

print("\nDay\tSalary")
print("----------------")

total_pay = 0.0
salary = 0.01

for day in range(1, days + 1):
    print(f"{day}\t${salary:.2f}")
    total_pay += salary
    salary *= 2

print("\nTotal pay: ${:.2f}".format(total_pay))
