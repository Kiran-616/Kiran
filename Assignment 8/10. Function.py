# Write a program to check if entered year is a leap year or not
def is_leap_year(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
        else:
            return True
    else:
        return False
    
# input from user

y = int(input("enter a year:"))

# function call

if is_leap_year(y):
    print(y, "is a leap year")
else:
    print(y, "is not a leap year")
