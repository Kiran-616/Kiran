# Accept age of five people and also per person ticket amount and then calculate total amount
total_amount = 0
for i in range(1,6):
    print(f"/nperson {i}:")
    age = int(input("Enter age:"))
    ticket_amount = float(input("Enter ticket amount:"))


    if age < 12:
        discount = 0.30 * ticket_amount
        print("Child - 30% discount applied")
    elif age > 59:
        discount = 0.50 * ticket_amount
        print("Senior citizen - 50% discount applied")
    else:
        discount = 0
        print("No discount")

    final_amount = ticket_amount - discount
    print(f"Final amount to pay: Rs {final_amount: .2f}") 
    total_amount += final_amount

    print(f"\nTotal amount for 5 people: Rs {total_amount:.2}")
