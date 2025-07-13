# Write a program to check if person is eligible to marry or not 
gender = input("Enter gender (male/female):").lower()
age = input("Enter age:")

if gender == "male":
    if age >= 21:
        print("you are eligible to marry")
elif gender == "female":
    if age >= 18:
        print("you are eligible to marry")
    else:
        print("you are not eligible to marry")
else:
    print("invalid gender entered")


