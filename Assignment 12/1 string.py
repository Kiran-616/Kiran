# Python program to replace all occurence of "a" with $ in a string
string = input("enter a string:")
new_string = ""
for char in string:
    if char == "a":
        new_string += "$"
    else:
        new_string += char
print("modified string:", new_string)