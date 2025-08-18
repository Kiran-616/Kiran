# python program to take in two strings and display the larger string without using built in functions
str1 = input("enter first string:")
str2 = input("enter second string:")

len1= 0
len2=0

for _ in str1:
    len1 +=1
for _ in str2:
    len2 +=1

if len1 > len2:
    print("larger string:" , str1)
elif len2 > len1:
    print("larger string: ", str2)
else:
    print("both strings are equal length")