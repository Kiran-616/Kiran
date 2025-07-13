# Write a program to accept year from user and check if it is a leap year or not

year = int(input("Enter the year"))
if year % 4 == 0:
    if year % 100 == 0:
        print("leap year:")

else:
    print("it is a not leap year")