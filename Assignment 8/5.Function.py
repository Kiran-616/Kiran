# Sum of all prime numbers between 1 to n
def prime(num):
    for i in range(2,num):
        if(num % i ==0):
            print("Not prime no:")
        else:
            print("it is  prime no:")
        return sum
    
num = int(input("enter the no:"))
ans = prime(num)
if(ans==num):
    print("no")
else:
    print("yes")