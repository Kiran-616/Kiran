# Write a program to find sum of digits using recrusion
def sumOfdigit(num):
    if (num==0):
        return 0
    
    else:
        a= num%10
        return a +sumOfdigit(num//10)
    

num= int(input("enter a number"))
print(sumOfdigit (num))