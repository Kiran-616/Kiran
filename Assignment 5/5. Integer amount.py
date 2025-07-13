# Write a program to accept an integer amount from user and tell minimum number of notes

amount = int(input("Enter the amount:"))

notes = [2000,500,200,100,50,20,10,5,2,1]

print("Minimum number of notes:")

for note in notes:
    if amount >= note:
        count = amount // note

        amount %= note
        print(f"{note} x {count}")
        