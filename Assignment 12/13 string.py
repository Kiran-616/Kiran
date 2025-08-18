# python program to count number of digits and letters in a string
string = input("enter a string:")
digit_count = 0
letter_count = 0

for ch in string:
    if "0" <= ch <= "9":
        digit_count +=1
    elif("a" <= ch <= "z" ) or ("A" <= ch <= "z"):
        letter_count += 1
print("digits: " ,digit_count)
print("letters:" , letter_count)