# Write a program to create a new list from existing list which contains cube of each number of list
original_list = [1,2,3,4,5]
cube_list =[]
for num in original_list:
    cube = num * num * num
    cube_list.append(cube)
print("list of cubes:" , cube_list)
