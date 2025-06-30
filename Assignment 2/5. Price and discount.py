# Calculate selling prize of book based on cost price and discount 
cost_price = float(input("Enter the cost price of the book:" ))
discount_percent = float(input("Enter the discount percentage:"))
discount_amount = (cost_price * discount_percent) / 100
selling_price = cost_price - discount_amount
print("selling price of the book is:", round(selling_price, 2))