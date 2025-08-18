#  Minimum number of notes

D = [2000,500,200,100,50,20,10,5]
amount = int(input("enter amount:"))
print("amount =", amount)

for note in D:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} x {count}")