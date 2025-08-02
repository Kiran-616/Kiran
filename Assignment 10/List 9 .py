# Write a program of having of elements in the list and find out even and odd elements in that list
n = int(input("how many elements do you want to enter in the list"))
original_list = []
even_list = []
odd_list = []

print("enter the elements:")
for i in range(n):
    num = int(input(f"element {i+1} :"))
    original_list.append(num)

for i in range(n):
    if original_list[i] % 2 == 0:
        even_list.append(original_list[i])
    else:
        odd_list.append(original_list[i])
print("original list:" , original_list)
print("even list:" , even_list)
print("odd list:" , odd_list)
