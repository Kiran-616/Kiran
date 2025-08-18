# python program to remove the nth index character from a non-empty string
string = input("enter a string:")
n = int(input("enter index to remove:"))
result= ""

for i in range(len(string)):
    if i != n:
        result += string[i]
print("after removing:" , result)