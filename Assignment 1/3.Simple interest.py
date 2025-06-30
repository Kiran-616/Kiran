# program to enter p , t , r and calculate simple interest
p = float(input("Enter Principle amount (P):"))
t = float(input("Enter Time in years (T):"))
r = float(input("Enter Rate of Interest (R):"))
si = (p * t * r) / 100
print("Simple Interest is:", si )
