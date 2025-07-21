# Write a program to calculate the sum of following series where n is input by user

#1/1! + 2/2! + 3/3! + 4/4! + .....N/N!

n = int(input("enter the value of n:"))
sum=0
fact=1

for i in range(1, n+1):
    fact = 1
    for j in range(1,n+1):
        fact *= j
    term = i/fact
    sum += term
print("sum of the series is:" , sum)

