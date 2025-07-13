# Input 5 subject mark from user and display grade (first class, second class)
m1 = float(input("Enter marks of subject 1:"))
m2 = float(input("Enter marks of subject 2 :"))
m3 = float(input("Enter marks of subject 3 :"))
m4 = float(input("Enter marks of subject 4 :"))
m5 = float(input("Enter markd of subject 5 :"))

total = m1 + m2 + m3 + m4 + m5 
percentage = (total / 500) * 100

print("Total marks = ", total)
print("Percentage = ",percentage)

if percentage >= 75:
    print("Grade: Distinction")

elif percentage >= 60:
    print("Grade: First class")
elif percentage >= 50:
    print("Grade:Second class ")
elif percentage >= 35:
    print("Grade: Pass class")
else:
    print("Grade:Fail")

