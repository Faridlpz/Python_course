meal_cost = 12.00
tip_percent = 20 
tax_percent = 8

tip = (meal_cost/100) * tip_percent
tax = tax_percent/100 * meal_cost
total_cost = meal_cost + tip + tax 
print(total_cost)
