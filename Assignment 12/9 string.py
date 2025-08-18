# python program to calculate the number of words and the number of characters present in a string
string = input('enter a string:')
char_count= 0
word_count = 1

for ch in string:
    if ch != " ":
        char_count += 1
    if ch == " ":
        word_count += 1
print("characters:" , char_count)
print("words:" , word_count)