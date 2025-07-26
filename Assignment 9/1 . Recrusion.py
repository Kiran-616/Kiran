# Write a program to find sum of following series using recursive functions:
# i . 1!+2!+3!+4+.
def factorial(n):
    if (n==0) or (n==1):
        return 1
    return n * factorial(n-1)

def series_sum(n):
    if n==0:
        return 0
    return factorial(n)+ series_sum(n-1)

n= int(input("enter n:"))
print("sum of series: " , series_sum (n))