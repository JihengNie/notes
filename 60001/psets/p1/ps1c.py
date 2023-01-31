# inputs
annual_salary = float(input('Enter the starting salary: '))

# functions

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

# state variables
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000.0
current_savings = 0
down_payment = 0.25 * total_cost
epsilon = 100

months = 0
bisection_count = 0
low = 0
high = 1.0
portion_saved = (high + low) / 2.0

# algorithm

if(annual_salary * 3 < down_payment):
    print('It is not possible to pay the down payment in three years.')
else:
  while abs(savings_after_3_years(annual_salary, portion_saved) - down_payment ) >= epsilon:
    if savings_after_3_years(annual_salary, portion_saved) < down_payment:
      low = portion_saved
    else:
      high = portion_saved
    portion_saved = (high + low) / 2.0
    bisection_count += 1
    print(portion_saved, bisection_count, savings_after_3_years(annual_salary, portion_saved))

  print('Best savings rate: ', portion_saved)
  print('Steps in bisection search: ', bisection_count)
