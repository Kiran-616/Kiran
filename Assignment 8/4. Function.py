# Sum of all odd numbers between 1 to n
def oddNumber(n):
    for i in range(1, n+1):
        if i % 2!=0:
            print(i)
    return oddNumber

# main program
n = int(input("enter the number:"))
result = oddNumber(n)
print(" oddNumbers up to n " , "are",
      oddNumber, (n))
      





    