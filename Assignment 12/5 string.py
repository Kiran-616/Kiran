# python program to count the number of vowels in a string
string = input("enter a string:")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1
print("number of vowels:" , count)