# Write a program to find the second largest element in the list
numbers = [10,40,30,20,50]
largest = second_largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

for num in numbers:
    if num != largest:
        if second_largest == largest or num > second_largest:
            second_largest = num
print ("second largest element is:" , second_largest)
        