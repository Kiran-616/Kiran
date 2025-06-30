# Write a program to swap two numbers using third variable
a = int(input("Enter first number (a):"))
b = int(input("Enter second number (b) :"))
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b 
b = temp
print("After swapping: a = ", a ," , b =", b)