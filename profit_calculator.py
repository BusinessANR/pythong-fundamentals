Sales = 4000

if Sales > 5000:
    print("Sales achieved within baseline")
else:
    print("Sales not achieved")


def calculate_profit(cost, revenue):
    profit = revenue - cost
    return profit

result=calculate_profit(5000, 4000)
print(result)
if result < 0:
    print("Loss incurred")
else:
    print("Profit made")

Product_name = "Detox drink"
Selling_Price = 30
profit_cost = 10

# Calculate profit 
profit = Selling_Price - profit_cost
print("product:", Product_name)
print("Selling Price:", Selling_Price)
print("Product cost:", profit_cost)
print("Profit:", profit)

if profit > 0:
    print("Profit made on product")
else:
    print("Loss incurred on product")