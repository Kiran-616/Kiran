text=input("enter a sentence:")
word_length = {word:len(word) for word in text.split()}
print("word lengths:",word_length)