# Write a program to calculate simple interest based on principle, rate and time 
principle = float (input("Enter the principle amount:"))
rate = float (input("Enter the rate of interest;"))
time = float (input ("Enter the time in years:"))

simple_interest = (principle * rate * time) / 100
print("simple interest =", simple_interest)