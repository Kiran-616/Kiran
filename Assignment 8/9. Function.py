# Write a program to check if entered number is a palindrome or not
def is_palindrome(num):
    original = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return original == reverse

# input from user
n = int(input("enter a number:"))

# function call
if is_palindrome(n):
    print(n,"is a palindrome number")
else:
    print(n, " is not a palindrome number")