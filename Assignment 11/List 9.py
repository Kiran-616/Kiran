# write a program to create three lists of numbers their squares and cubes
n = int(input("enter how many numbers you want to enter:"))

number_list =[]
square_list = []
cube_list = []

print("enter the numbers:")
for i in range(n):
    num = int(input(f"element{i+1} :"))
    number_list.append(num)
    square_list.append(num **2)
    cube_list.append(num ** 3)

print("original numbers list:" , number_list)
print("squares list:" , square_list)
print("cubes list:" , cube_list)