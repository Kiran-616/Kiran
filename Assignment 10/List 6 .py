# Write a program to remove duplicates from the list
original_list = [10,20,10,30,40,20,50,30]

unique_list =[]

for item in original_list:
    found = False
    for u in unique_list:
        if item == u:
            found = True
            break
    if not found:
        unique_list.append(item)

    print("list after removing duplicates:" , unique_list)