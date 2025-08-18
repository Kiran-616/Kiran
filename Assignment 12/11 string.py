# python program to replace every blank space with hyphen in a string
string = input("enter a string:")
chars = list(string)

for i in range(len(chars)):
    if chars[i] == " ":
        chars[i] = "_"

result = "".join(chars)
print("modified string: " ,result)