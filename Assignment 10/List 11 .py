# Write a program to print all numbers which are divisible by m and nn in the list

size = int(input("enter the number of elements in the list:"))
num_list = []
print("enter the elements:")
for i in range(size):
    element = int(input(f"{i+1}:"))
    num_list.append(element)

m = int(input("enter the value of m:"))
n = int(input("enter the value of n:"))

print(f"numbers divisible by both{m} and{n} are:")

for i in range(size):
    if num_list[i] % m == 0 and num_list[i] % n == 0:
        print(num_list [i])