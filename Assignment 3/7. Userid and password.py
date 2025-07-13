# Write a program to check if user has entered correct userid and password
correct_user_id = "kiran"
correct_password = "kiran@2003"

user_id = input("Enter user Id:")
password = input("Enter password ")

if user_id == correct_user_id and password == correct_password:
    print("Login successful!!")
else:
    print("Invalid user ID or Password")