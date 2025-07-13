# Enter number of students from user. for those many students accept marks of 5 subject marks from user calculate percentage

num_students = int(input("Enter number of students:"))
 
total_percentage = 0
for i in range(1 , num_students + 1):
    print(f"\ n enter marks for student {i} (out of 100 each subject):")
    total_marks = 0

    for j in range (1 , 6):
        marks = float(input(f" subject {j} marks: "))
        total_marks += marks

        percentage = (total_marks / 500)* 100
        total_percentage += percentage 

        print(f" percentage of student {i}:. {percentage: 2f} %") 
average_percentage = total_percentage / num_students       

print(f" \nAverage percentage of all students : {average_percentage :. 2f }%")
