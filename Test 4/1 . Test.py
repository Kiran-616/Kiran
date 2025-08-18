# Write a function to which we pass a parameter and prints the factors of a given number

def fact():
    num = int(input("Enter a number:"))
    fact = 1
    for i in range (1, num + 1):
         fact *=i
    return fact

result = fact()
print("factorial is ",result)

    

