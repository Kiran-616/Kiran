# Write a program to print first n prime numbers
num = int(input("enter number:"))
for i in range(2,num):
    if(num % i ==0):
        print("Not prime number")
        break
else:
        print("prime number")
        