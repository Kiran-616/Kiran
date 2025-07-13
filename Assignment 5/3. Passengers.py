# Accept no . of passengers from user and per ticket cost
num_passengers = int(input("Enter number of passengers:"))
ticket_cost = float(input("Enter cost per ticket:"))

total_amount = 0
for i in range (1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}:"))

    if age < 12:
        discount = 0.30
    elif age > 59:
        discount = 0.50
    else:
        discount = 0.0
    
    final_cost = ticket_cost * (1 - discount)
    total_amount += final_cost

    print(f"ticket for passenger {i } after discount : Rs{final_cost: 2f}")

    print(f"\n total amount to be paid for all passengers: Rs{total_amount: 2f}")