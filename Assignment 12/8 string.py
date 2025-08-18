# python programs to remove the characters of odd index values in a string
string = input('enter a string:')
result = ""

for i in range(len(string)):
    if i % 2 ==0:
        result += string[i]
print("after removing odd index chars:" , result)