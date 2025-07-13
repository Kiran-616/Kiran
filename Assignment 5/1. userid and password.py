# Write a program user to enter userid and password. if id and password is incorrect give him chance to reenter the credentails

correct_userid = "admin"
correct_password = "1234" 

for attempt in range(1,4):
    userid = input("Enter user ID:")
    password = input("Enter password:")

    if userid == correct_userid and password == correct_password:
        print("Login sucessful Welcome.")
        break
    else:
        print(f"Incorrect credentials . Attempt {attempt} of 3 ./ n")
else:
    print("3 incorrect attempts program terminated")