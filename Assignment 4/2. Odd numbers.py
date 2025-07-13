# Wap to print all odd numbers until n
n = int(input("Enter the number:"))

print ("odd numbers up to", n ," are :")
for i in range (1, n+1):
    if i % 2 != 0:
        print(i)



