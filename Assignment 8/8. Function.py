# Write a program find reverse of a number

def reverse_number(num):
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    return reverse

# input from user

n = int(input("enter a number:"))
result = reverse_number(n)

print("reverse of the number is:" , result)
