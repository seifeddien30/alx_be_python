monthly_income = int(input("Enter your monthly income: "))
monthly_epneses = int(input("Enter your total monthly expenses: "))
monthly_saving = monthly_income - monthly_epneses

projected_saving = int(monthly_saving * 12 + (monthly_saving * 12 * 0.05))
print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected savings after one year, with interest, is: ${projected_saving}.")


#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))