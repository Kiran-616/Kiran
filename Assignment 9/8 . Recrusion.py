# Write a program to check whether a number is prime or not using recrusion
def is_prime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5) +1):
        if n % i ==0:
            return False
        return True
    
num = int(input("enter number:"))
if is_prime(num):
    print("prime number")

else:
    print("not a prime number:")
