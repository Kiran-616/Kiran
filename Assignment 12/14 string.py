# python program to count the occurences of ach word in a string
string = input("enter a string:")
words = string.spilt(" ")
word_count = {}

for word in words:
    word_count [word] = word_count = {}
word_count.get(word,0)+1

for word, count in word_count.items():
    print(word,":" , count)