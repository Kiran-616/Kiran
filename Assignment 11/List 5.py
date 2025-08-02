# python program to sort a list according to the length of the elements within the list
n = int(input("enter number of elements in the list:"))

input_list = []
print("enter the string elements:")
for i in range(n):
    element = input(f"element{i+1} :")
    input_list.append(element)

sorted_list = sorted(input_list , key = len)

print("original list:" , input_list)
print("sorted list by length:" , sorted_list)
