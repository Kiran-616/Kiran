# Wap to check if given number is perfect number
num = int(input("Enter the number:"))

sum_of_divisors = 0

for i in range (1, num):
    if num % i == 0:
       sum_of_divisors += i

if sum_of_divisors == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")
