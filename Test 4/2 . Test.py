# write a program to find factorial of all no in given range using recrusion

def factorial(n):
    if(n==1):
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input("enter a number"))
x = factorial(n)
print(x)


