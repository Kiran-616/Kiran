# write a program to print list after removing even numbers
n = int(input("enter how many elements you want to add:"))
original_list =[]
print("enter the numbers:")
for i in range(n):
    num = int(input(f"element{i+1}:"))
    original_list.append(num)
filtered_list = [x for x in original_list if x % 2 != 0]

print("original list:" , original_list)
print("list after removing even numbers:" , filtered_list)