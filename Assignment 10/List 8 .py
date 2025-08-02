# Write a program to create a duplicaate of an existing list.it should not point to same list
original_list = [10,20,30,40,50]
duplicate_list = []
for item in original_list:
    duplicate_list.append(item)

print("original list:" , original_list)
print("duplicate list:" , duplicate_list)
print("are both lists different objects in memory" , original_list is not duplicate_list)