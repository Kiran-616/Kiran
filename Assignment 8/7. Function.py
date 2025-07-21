# Write a program to find sum of digits of a number
def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num//10
    return total

# input from user

n= int(input("enter a number:"))
result = sum_of_digits(n)
print("sum of digits:" , result)

