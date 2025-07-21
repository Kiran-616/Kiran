# Write a program to find sum of following series using functions

# a. 1+2+3+4+.......+n

def  find_sum (n):
    total = 0
    for i in range(1, n + 1):
        total+=i
    return total

# main program
num = int(input("enter the value of n"))
result = find_sum(num)
print("sum of series 1+2+......+n",
num, "=" , (result))

# b.1 !+ 2! +......+n
def factorial (num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

def sum_of_factorial(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
# main
num = int(input("enter a number:"))
print("sum of factorials =" , sum_of_factorial (num))

# c. 1^1 + 2^2 + 3^3 + ....+ n ^ n 

def sum_power_series(n):
    total = 0
    for i in range (1, n +1):
     return total
    
# main
num= int(input("enter a number:"))
print("sum of power series =" , sum_power_series (num))

