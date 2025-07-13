# Write a program to promot user to enter userid and password
import random
correct_user = "kiran" 
correct_pass = "kiran@2003"


user_id = int(input("Enter  user_id:"))
password = int(input("Enter pass:"))

if user_id == correct_user and password == correct_pass:
    print("Login successful!!")

    captcha = random.randint(1111,9999)
    entered_captcha = int(input("Enter the captcha number shown above:"))

    if entered_captcha == captcha:
        print("Access granted (captcha verifird)")
    else:
        print("Access denied (captcha mismatch)")

else :
    print("Invalid user ID or password")
    




