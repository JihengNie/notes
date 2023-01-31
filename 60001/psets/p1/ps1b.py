# inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter as a decimal percentage: "))

# state variables
portion_down_payment = .25 * total_cost
r = .04
months = 0
current_savings = 0.0

# algorithm
while current_savings < portion_down_payment:
  if months >= 6 and months % 6 == 0 :
    annual_salary = annual_salary + annual_salary * semi_annual_raise

  annual_return_from_savings = current_savings * r / 12
  salary_saved_per_month = annual_salary * portion_saved / 12

  current_savings = current_savings + annual_return_from_savings + salary_saved_per_month
  months += 1
  print(current_savings, months, annual_salary)

print(months)
