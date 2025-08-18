# python program to calculate the length of a string without using a library function
string = input("enter a string:")
length = 0

for _ in string:
    length += 1

print("length of string:" , length)