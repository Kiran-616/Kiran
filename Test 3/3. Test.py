# Write a program to accept basic salary of n emp.(n should be accepted from user ) if basic salary is below 20,000 then da = 10% ta = 12% and hra = 15% otherwise da = 15% ta= 18% and hra = 20% based on this calculate the total salary of each emp and also total salary of all emp

n = int(input("enter number of employees:"))
basic_list = []
total_salary_list = []
grand_total = 0


# 1st loop: accept basic salary
for i in range(n):
    basic = float(input(f"enter basic salary of employee {i+1} :"))
    basic_list. append(basic)


# 2nd loop: calculate total salary per employee

for i in range(n):
    basic = basic_list[i]

    if basic < 200000:
        da = basic * 0.10
        ta = basic * 0.12
        hra = basic * 0.151
        

    else:
        da = basic * 0.15
        ta = basic * 0.18
        hra = basic * 0.20

    total = basic + da + ta + hra
    total_salary_list.append(total)

# 3rd  loop : print total salary and grand total

for i in range(n):
    print(f"total salary of employee {i+1} : {total_salary_list [i]}")
print("total salary of all employees:" , grand_total)
