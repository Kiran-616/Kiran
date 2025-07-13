# Write a program to accept 3 digit number . if first digit is double of second digit and half of third digit then display
num = int(input("Enter a 3-digit number:"))

first = num // 100
second = (num //10) % 10
third = num % 10


if first == 2 * second and first == third / 2:
    
    print("yes , you have done it")
else:
    print("please try next time")