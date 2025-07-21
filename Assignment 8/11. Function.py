# Wap to check if a given number is armstrong number or not. for each task create seperate functions

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

# function to calculate power
def power (base, exp):
    result = 1

    for _ in range (exp):
        result = 1
        for _ in range(exp):
            result= 1
            for _ in range(exp):
                result = 1
                for _ in range (exp):
                    result *= base
                return result
            
# function to calculate sum of digits raised to power of total digits

def sum_of_digit_powers(num):
    n = count_digits(num)
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += power (digit, n)
        temp = temp // 10
    return total

# function to check armstrong

def is_armstrong(num):
     return num == \
sum_of_digit_powers(num)




    
 

# main part
number = int(input("enter a number:"))
if is_armstrong(number):
    print(number, "is an armstrong number")
else:
    print(number, "is not an armstrong number")


