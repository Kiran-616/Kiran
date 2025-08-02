# python program to put even of a list into two different lists
n = int(input("enter how many elements you want in the list:"))
original_list = []
print("enter the elements:")
for i in range(n):
    num = int(input(f"element{i+1} :"))
    original_list.append(num)
even_list = []
for i in range(n):
    if original_list[i] % 2 == 0:
        even_list.append(original_list[i])
mid = len(even_list) // 2
even_list1 = []
even_list2 = []
for i in range(len(even_list)):
    if i < mid:
        even_list1.append(even_list[i])
    else:
        even_list2.append(even_list[i])

print("original list:" , original_list)
print("all even numbers:" , even_list)
print("even list 1 (first half):" , even_list1)
print("even list 2 (second half) :", even_list2) 
