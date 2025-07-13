# Write a program to check if given 3 digit number is a palindrome or not
number = int(input("Enter a 3-digit number:"))
original_number = number

reverse = 0
while number > 0:
    digit = number % 10
    reverse = (reverse * 10) + digit 
    number = number // 10
if original_number == reverse:
    print(f"{original_number } is a palindrome.")
else:
    print(f"{original_number} is not a palindrome")
