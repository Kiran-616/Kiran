# Accept a number from user and check if this element is present in the list or not also tell how many times it is present in the list
numbers = [5,10,20,10,30,10,40]
target = int(input("enter the number to search:"))

count = 0
for num in numbers:
    if num == target :
        count +=1
if count>0:
    print(target, "is present in the list")
    print("it appears", count, "times")
else:
    print(target, "is not present in the list")
