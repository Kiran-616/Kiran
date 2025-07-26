# Write a program to reverse a given number using recursive function

def reverse(num,rev):
    if num!=0:
        a   = num  % 10
        rev = rev  * 10  + a
        return reverse(num // 10, rev)

    else:
        return rev
    
num = int(input("enter a number"))
ans = reverse(num , 0)
print("reversed number:" , ans)
