# python program to take in a string and replace every blank space with hyphen
string = input("enter a string:")
result = ""

for ch in string:
    if ch == " ":
        result += "-"
    else:
        result += ch
print("modified string:" , result)