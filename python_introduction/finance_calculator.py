# User input for income and expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projected savings assuming a 5% increase in savings
projected_savings = monthly_savings * 12 + int(monthly_savings * 0.05 * 12)

print("Your projected savings for the year is:", projected_savings) 