# Dillon Matthews
# This program calculates the distance a car can travel on a full tank of gas.

gas_tank_capacity = 21
town_mpg = 23.5
highway_mpg = 28.9

town_distance = (1 / 3) * gas_tank_capacity * town_mpg
highway_distance = (2 / 3) * gas_tank_capacity * highway_mpg
total_distance = town_distance + highway_distance

print("The total distance the car can travel is:", total_distance, "miles")
