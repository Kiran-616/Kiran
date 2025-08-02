# Write a program to create three lists of numbers their squares and cubes
n = int(input("enter how many numbers you want to enter:"))

number_list =[]
square_list =[]
cube_list =[]

print("enter the numbers:")
for i in range(n):
    num = int(input(f"element {i+1}:"))
    number_list.append(num)

    square = num * num
    cube = num * num * num

    square_list.append(square)
    cube_list.append(cube)

print("original numbers:" , number_list)
print("squares:" , square_list)
print("cubes:" , cube_list)