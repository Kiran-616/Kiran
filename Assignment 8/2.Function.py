# Write a program to calculate area of circle

def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area

# input from user

r = float(input("enter radius of the circle:"))
result = area_of_circle(r)
print("area of the circle is:" , result)
