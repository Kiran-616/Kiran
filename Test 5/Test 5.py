#  union of two lists(without set)

list1 = [1,2,3,4]
list2 = [3,4,5,6]

union_list = list1[:]

for x in list2:
    if x not in union_list:
        union_list.append(x)
print("union:" , union_list)