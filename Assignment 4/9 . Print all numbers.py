# Wap to print all numbers in a range divisible by a given number
start = int(input("Enter starting number:"))
end = int(input("Enter ending number:"))

divisor = int(input("Enter the number to divide by:"))

print("Numbers divisible by", divisor, "from", start, "to", end,"are:")

for i in range (start, end + 1):
    if i % divisor == 0:
        print(i)