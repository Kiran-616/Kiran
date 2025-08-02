# Write a program to remove all occurences of a given element in the list
n = int(input("enter the number of elements in the list:"))
original_list = []
print("enter the elements:")
for i in range(n):
    num = int(input(f"element {i+1}:"))
    original_list.append(num)
target = int(input("enter the element to remove from the list:"))

new_list = []
for i in range(n):
    if original_list[i] != target:
        new_list.append(original_list[i])
print("original list:" , original_list)
print("list after removing all occurences of" , target , ":" , new_list)
