# Program to find the roots of a quadratic equation
import math
a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d )) / (2*a)
    print("Roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 = ", root2)
elif d == 0:
    root = -b / (2*a)
    print("Roots are real and equal.")
    print("Roots =",root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-d ) / (2*a)
    print("Roots are complex and imaginary.")
    print("Root 1 =", real_part, "+", imag_part, "i")
    print("Root 2 =", real_part, "-" , imag_part, "i")
          






          