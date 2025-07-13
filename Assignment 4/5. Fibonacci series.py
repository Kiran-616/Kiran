# Wap to print fibonacci series upto n
n = int(input('Enter the number of terms:'))

a, b = 0, 1
count = 0

print("Fibonacci series up to", n,"terms is:")

while count < n:
    print(a)
    c = a+b
    a=b
    b= c
    count += 1