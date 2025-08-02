# python program to find the second largest number in a list using bubble sort
n = int(input("enter number of elements in the list:"))
num_list =[]

print("enter the elements:")
for i in range(n):
    num = int(input(f"element {i+1} :"))
    num_list.append(num)

for i in range(n):
    for j in range(0, n -i-1):
        if num_list[j] < num_list[j+1]:
            temp = num_list[j]
            num_list[j] = num_list[j+1]
first_largest = num_list[0]
second_largest = None

for i in range(1,n):
    if num_list[i] != first_largest:
        second_largest = num_list[i]
        break 
print("sorted list (descending):" , num_list)
if second_largest is not None:
    print("second largest number is:" , second_largest)
else:print("all elements are the same . No second largest number.")