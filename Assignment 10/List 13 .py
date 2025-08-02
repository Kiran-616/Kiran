# Write a program to print list after removing even numbers
n = int(input("enter the number of elements:"))

original_list = []
print("enter the elements:")
for i in range(n):
    num = int(input(f"element{i+1}:"))
    original_list.append(num)
odd_list = []
for i in range(n):
    if original_list[i] % 2 !=0:
        odd_list.append(original_list[i])

print("original list:" , original_list)
print("list after removing even numbers:" , odd_list)