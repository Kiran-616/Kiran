# A man goes for shopping . he buys 5 products accepts the price of all products and display the total bill after adding
prices = []
for i in range(1 , 6):
    price = float(input("Enter price of product {i}:"))
    prices.append(price)
total = sum(prices) 
gst = total * 0.18
total_bill = total + gst

print("Total bill after adding 18% gst is Rs.", round(total_bill,2))
