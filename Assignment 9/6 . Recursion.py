# Write a program to print fibonacci series using recursion
def fibbo(a,b,n):
    if(n>0):
        c = a+b
        print(c)
        fibbo(b,c,n-1)

n=int(input("enter a number:"))

fibbo(-1,1,n)
