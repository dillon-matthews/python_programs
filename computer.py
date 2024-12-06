# Dillon Matthews
# This program calculates and formats a report based on the Build a Computer Assignment complete with costs, total cost, and monthly payments.

# Features and costs
cpu = 339
ram = 561
primary_storage = 130
secondary_storage = 90
video_card = 840
power_supply = 130
case = 125
keyboard = 130
mouse = 100
primary_monitor = 700
secondary_monitor = 143
printer = 40
connectivity = 99
cooling = 120

# Calculate total cost and monthly payment
total_cost = cpu + ram + primary_storage + secondary_storage + video_card + power_supply + case + keyboard + mouse + primary_monitor + secondary_monitor + printer + connectivity + cooling
monthly_payment = total_cost / 12

# Print the report
print("\nMy Dream Computer will have these features and costs.\n")
print(f"{'FEATURE':<20}\t\t{'COST'}")
print(f"{'-'*20}\t\t{'-'*8}")
print(f"{'CPU':<20}\t\t${cpu:.2f}")
print(f"{'RAM':<20}\t\t${ram:.2f}")
print(f"{'Primary Storage':<20}\t\t${primary_storage:.2f}")
print(f"{'Secondary Storage':<20}\t\t${secondary_storage:.2f}")
print(f"{'Video Card':<20}\t\t${video_card:.2f}")
print(f"{'Power Supply':<20}\t\t${power_supply:.2f}")
print(f"{'Case':<20}\t\t${case:.2f}")
print(f"{'Keyboard':<20}\t\t${keyboard:.2f}")
print(f"{'Mouse':<20}\t\t${mouse:.2f}")
print(f"{'Primary Monitor':<20}\t\t${primary_monitor:.2f}")
print(f"{'Secondary Monitor':<20}\t\t${secondary_monitor:.2f}")
print(f"{'Printer':<20}\t\t${printer:.2f}")
print(f"{'Ports/Connectivity':<20}\t\t${connectivity:.2f}")
print(f"{'Cooling':<20}\t\t${cooling:.2f}")
print(f"\n{'TOTAL COST':<20}\t\t${total_cost:.2f}")
print(f"{'Monthly Payments':<20}\t\t${monthly_payment:.2f}")
