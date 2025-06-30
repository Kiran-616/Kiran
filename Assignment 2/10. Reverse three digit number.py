# Write a program to reverse three digit number
number = int(input("Enter a 3- digit number:"))
hundreds = number // 100
tens = (number % 100) // 10
units = number % 10
reversed_number = (units * 100) + (tens * 10) + hundreds
print("Reversed number is: " , reversed_number)