# Find all the unique words and count the frequency of occurence from a given list of strings use python set data type
words = ["apple" , "banana" , "apple" , "banana" , "apple"]
unique_words = set(words)
print("unique_words:" , unique_words)
for word in unique_words:
    print(word, ":" , words.count(word))