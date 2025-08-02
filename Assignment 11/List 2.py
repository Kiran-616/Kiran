# python program to merge two lists and sort it
n1 = int(input("enter number of elements in list 1:"))
list1 = []
print("enter elements for list 1:")
for i in range(n1):
    num = int(input(f"element{i+1 } :"))
    list1.append(num)

n2 = int(input("enter number of elements in list 2:"))
list2 =[]
print("enter elements for list 2:")
for i in range(n2):
    num = int(input(f"element{i+1}:"))
    list2.append(num)
merged_list = list1 + list2
merged_list.sort()

print("list 1:" , list1)
print("list2:" , list2)
print("merged and sorted list:" , merged_list)