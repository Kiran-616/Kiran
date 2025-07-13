# Wap to print factorial of a number
n = int(input("Enter the number:"))

factorial = 1
for i in range (1, n + 1):

    factorial *= i
print("The factorial of", n,"is:",factorial)
