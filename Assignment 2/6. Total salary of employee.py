# To calculate total salary of employee based on basic ,da=10% of basic, ta=12% of basic ,hra=15% of basic
basic_salary = float(input("Enter the basic salary of the employee:"))
da = (10 / 100 ) * basic_salary
ta = (12 / 100 ) * basic_salary
hra = (15 / 100 )* basic_salary
total_salary = basic_salary + da + ta + hra
print("Dearness Allowance (DA):" , da)
print("Travel Allowance (TA): ", ta)
print("House Rent Allowance (HRA): ", hra)
print("Total salary is: ", round(total_salary, 2))