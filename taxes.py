# Dillon Matthews
# This program calculates the taxes owed based on filing status and taxable income.

def calculate_taxes():
    # Tax brackets for each filing status
    tax_brackets = {
        "single": [
            (9875, 0.10),
            (40125, 0.12),
            (85525, 0.22),
            (163300, 0.24),
            (207350, 0.32),
            (518400, 0.35),
            (float('inf'), 0.37),
        ],
        "married_jointly": [
            (19750, 0.10),
            (80250, 0.12),
            (171050, 0.22),
            (326600, 0.24),
            (414700, 0.32),
            (622050, 0.35),
            (float('inf'), 0.37),
        ],
        "married_separately": [
            (9875, 0.10),
            (40125, 0.12),
            (85525, 0.22),
            (163300, 0.24),
            (207350, 0.32),
            (518400, 0.35),
            (float('inf'), 0.37),
        ],
        "head_of_household": [
            (14100, 0.10),
            (53700, 0.12),
            (85500, 0.22),
            (163300, 0.24),
            (207350, 0.32),
            (518400, 0.35),
            (float('inf'), 0.37),
        ],
    }

    # Prompt user for filing status and taxable income
    print("Filing Status Options: single, married_jointly, married_separately, head_of_household")
    filing_status = input("Enter your filing status: ").lower()
    income = float(input("Enter your taxable income: "))

    # Validate filing status
    if filing_status not in tax_brackets:
        print("Invalid filing status. Please enter a valid status.")
        return

    # Calculate taxes
    brackets = tax_brackets[filing_status]
    taxes = 0.0
    prev_limit = 0

    for limit, rate in brackets:
        if income > limit:
            taxes += (limit - prev_limit) * rate
            prev_limit = limit
        else:
            taxes += (income - prev_limit) * rate
            break

    # Display the amount of taxes owed
    print(f"The amount of taxes you owe is: ${taxes:.2f}")

# Run the tax calculator
calculate_taxes()
