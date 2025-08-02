# python program to find the intersection of two lists 
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

intersection_list = []

for i in range(len(list1)):
    if list1[i] in list2 and list1[i] not in intersection_list:
        intersection_list.append(list1[i])

print("list1:" , list1)
print("list2:" , list2)
print("intersection of both lists:" , intersection_list)
 
