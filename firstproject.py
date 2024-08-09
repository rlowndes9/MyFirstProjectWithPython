# Define earned amounts as a dictionary
earned_amounts = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}

# Calculate total income
total_income = sum(earned_amounts.values())

# Print earned amounts
print("Earned amount:")
for item, amount in earned_amounts.items():
    print(f"{item}: ${amount}")

# Print total income
print(f"\nTotal Income: ${total_income}")

# Get user input for expenses
staff_expenses = int(input("Enter staff expenses: "))
other_expenses = int(input("Enter other expenses: "))

# Calculate net income
net_income = total_income - (staff_expenses + other_expenses)

# Print net income
print(f"Net Income: ${net_income}")
