def approximate_sqrt(n):
    if n < 0:
        return "Invalid input. Square root of negative numbers is not real."
    if n == 0:
        return 0
    last_guess = n / 2
    next_guess = (last_guess + (n / last_guess)) / 2
    while abs(next_guess - last_guess) >= 0.0001:
        last_guess = next_guess
        next_guess = (last_guess + (n / last_guess)) / 2
    return round(next_guess, 4)

number = float(input("Enter a number to approximate its square root: "))
result = approximate_sqrt(number)
print(f"The approximate square root of {number} is {result}.")
