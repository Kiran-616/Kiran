# python program to count number of lowercase characters in a string
string = input("enter a string:")
count = 0

for ch in string:
    if "a" <= ch <= "z":
        count +=1
print("lowercase letters count:" , count)
