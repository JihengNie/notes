# inputs
annual_salary = float(input("Enter your annual salary: "))

# state variables
semi_annual_raise = .07
r = .04
total_cost = 1000000
down_payment = .25 * total_cost
current_savings = 0.0
number_of_months = 36

# Months Function
def how_many_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
  # state variables
  portion_down_payment = .25 * total_cost
  r = .04
  months = 0
  current_savings = 0.0
  result = [None] * 2

  # algorithm
  while current_savings < portion_down_payment:
    if months >= 6 and months % 6 == 0 :
      annual_salary = annual_salary + annual_salary * semi_annual_raise

    annual_return_from_savings = current_savings * r / 12
    salary_saved_per_month = annual_salary * portion_saved / 12

    current_savings = current_savings + annual_return_from_savings + salary_saved_per_month
    months += 1
    # print(current_savings, months, annual_salary)
    if months == 36:
      result[0] = current_savings

  if result[0] == None:
    result[0] = current_savings
  result[1] = months
  return result

# print(how_many_months( 120000.0, .05000,  500000.0, .03))

# algorithm
steps = 0
loop = True
end_point = 10000
start_point = 0
tolerence = 100
midpoint = (end_point - start_point ) / 2
new_end_point = start_point + midpoint

# Initial check
if how_many_months(annual_salary, 1, total_cost, semi_annual_raise)[1] > 36:
  print("Not enough salary")

if abs(how_many_months(annual_salary, end_point, total_cost, semi_annual_raise)[0] - down_payment) <= tolerence:
    print(steps)

# variables


while loop = True:
  if abs(how_many_months(annual_salary, new_end_point, total_cost, semi_annual_raise)[0] - down_payment) <= tolerence:
    print(steps)
  steps =+ 1
  midpoint = (new_end_point - start_point ) / 2
  new_end_point = start_point + midpoint
