# python program to detect if two strings are anagrams
str1 = input("enter first string:")
str2 =input("enter second string:")

if len(str1)!= len(str2):
    print("not anagrams")
else:
    count1 = {}
    count2 = {}
    for ch in str1:
        count1[ch] = count1.get(ch,0)+1
    for ch in str2:
        count2[ch] = count2.get(ch,0)+1
    if  count1 == count2:
        print("Anagrams")
    else:
        print("Not anagrams")
    

    