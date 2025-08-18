# python program to form a new string where the first character and the last character have been exchanged
string = input("enter a string:")
if len (string) <=1:
    print("result:" , string)
else:
    result = string[-1]+ string[1:-1]+string[0]
    print("result:" , result)