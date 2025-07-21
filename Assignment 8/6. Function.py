# Write a program to find print the following fibonaic series using functionc
# 1 1 2 3 5 8 n terms

def fibonacci_series(n):
    a , b = 1,1
    print(a,b, end= " ")
    for  _ in range(2,n):
        c = a + b
        print(c , end=" ")
        a = b
        b = c

# input from user
n= int(input("enter number of terms:"))
if n >= 1:
    fibonacci_series(n)
else:
    print("please enter a number greater than 0 .")

