# program to enter p , t , r and calculate compound interest
p = float(input("Enter Principle amount (P): "))
t = float(input("Enter Time in years (T): ")) 
r = float(input("Enter Rate of Interest (R): "))
amount = p * (1 + r / 100) ** t
ci = amount - p 
print("Compound Interest is:", ci)
