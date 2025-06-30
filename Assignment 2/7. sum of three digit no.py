# Find the sum of three digit number
number = int(input("Enter a 3-digit number: "))
hundreds = number // 100
tens = (number % 100) // 10
units = number % 10
digit_sum = hundreds + tens + units
print("Sum of digits is:" , digit_sum)
