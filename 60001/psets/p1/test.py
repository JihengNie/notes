# inputs
annual_salary = float(input('Enter the starting salary: '))
portion_saved = float(input('Enter the portion saved: '))

def savings_after_3_years(annual_salary, portion_saved):
  down_payment = 0.25
  total_cost = 1000000.0
  semi_annual_raise = 0.07
  portion_down_payment = down_payment * total_cost
  r = .04
  months = 0
  current_savings = 0.0
  while months < 36:
    if months >= 6 and months % 6 == 0 :
      annual_salary = annual_salary + annual_salary * semi_annual_raise

    annual_return_from_savings = current_savings * r / 12
    salary_saved_per_month = annual_salary * portion_saved / 12

    current_savings = current_savings + annual_return_from_savings + salary_saved_per_month
    months += 1
  return current_savings

print(savings_after_3_years(annual_salary, portion_saved))

total_cost = 1000000.0
current_savings = 0
down_payment = 0.25 * total_cost
print(down_payment)
