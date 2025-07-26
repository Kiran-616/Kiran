# Write a program to find sum of n numbers using recrusion
def sum_n(n):
    if n==0:
        return 0
    return n +sum_n (n-1)

n=int(input("enter n:"))
print("sum" ,sum_n (n))