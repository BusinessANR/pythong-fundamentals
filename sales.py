
from unicodedata import category


sales_data = [
    {"product": "Massage Cream", "category": "Wellness", "price": 39.90, "cost": 15.00, "quantity": 120},
    {"product": "Facial Cleanser", "category": "Skincare", "price": 29.90, "cost": 12.00, "quantity": 85},
    {"product": "Body Scrub", "category": "Wellness", "price": 45.00, "cost": 18.00, "quantity": 65},
    {"product": "Cuticle Oil", "category": "Nails", "price": 19.90, "cost": 7.00, "quantity": 150},
    {"product": "Heel Repair Cream", "category": "Wellness", "price": 35.00, "cost": 14.00, "quantity": 95},
    {"product": "Facial Serum", "category": "Skincare", "price": 59.90, "cost": 25.00, "quantity": 70},
    {"product": "Nail Polish", "category": "Nails", "price": 15.00, "cost": 5.00, "quantity": 200},
    {"product": "Massage Oil", "category": "Wellness", "price": 49.90, "cost": 20.00, "quantity": 110},
    {"product": "Face Mask", "category": "Skincare", "price": 12.90, "cost": 4.00, "quantity": 180},
    {"product": "Hand Cream", "category": "Skincare", "price": 25.00, "cost": 10.00, "quantity": 90}]

for product in sales_data:
    product["Revenue"] = (product["price"] * product["quantity"])
    product["profit"] = product["Revenue"] - (product["cost"] * product["quantity"])
    product["quantity sold"] = product["quantity"]

print("Products:", [product["product"] for product in sales_data])
print("Product costs:", [product["cost"] for product in sales_data])
print("Product quantity (sales):", [product["quantity"] for product in sales_data])


print("Revenue for each product:", [product["Revenue"] for product in sales_data])
print("Profit for each product:", [product["profit"] for product in sales_data])
print("Quantity sold for each product:", [product["quantity sold"] for product in sales_data])

for product in sales_data:
    if product["profit"] > 0:
        print(f"{product['product']} is profitable with a profit of ${product['profit']:.2f}.")
    else:
        print(f"{product['product']} is not profitable with a loss of ${-product['profit']:.2f}.")


category_product = {}
for product in sales_data:
    sort_category = product["category"]
    if sort_category not in category_product:
        category_product[sort_category] = []


category_revenue = {}
for product in sales_data:
    category = product["category"]
    if category not in category_revenue:
        category_revenue[category] = 0
    category_revenue[category] += product["Revenue"]

    category_profit = {}
for product in sales_data:
    category = product["category"]
    if category not in category_profit:
        category_profit[category] = 0
    category_profit[category] += product["profit"]


category
print("Revenue by category:", category_revenue)
print("Profit by category:", category_profit)
print("margin by category:", {category: (category_profit[category] / category_revenue[category]) * 100 for category in category_revenue})


