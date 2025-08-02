# Write a program to reverse the list
original_list = [10,20,30,40,50]
reversed_list = []

index = len(original_list) - 1
while index >= 0:

    reversed_list.append(original_list [index])
    index -= 1
print("reversed list:" , reversed_list)