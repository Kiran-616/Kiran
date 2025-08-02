# Write a program to find maximum and minimum element im a list
 
numbers = [10,50,25,90,5,70]
maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("maximum element is:" , maximum)
print("minimum element is:" , minimum)