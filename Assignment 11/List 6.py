# python program to find the union of two lists
list1 = [1,2,3,4]
list2 = [3,4,5,6]

union_list = list(set(list1+list2))

print("list1: ", list1)
print("list2:" , list2)
print("union of both lists:", union_list)