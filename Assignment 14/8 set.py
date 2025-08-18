# group anagrams

words = ["bat" , "tab" , "cat" , "act" ,"tac" , "rat"]

anagrams = {}

for word in words:
    key = "" .join(sorted(word))
    anagrams.setdefault(key,[] .append(word))

print("grouped anagrams:")
for group in anagrams.values():
    print(group)