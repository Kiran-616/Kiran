# Write a program to calculate area of rectangle
def areaOfrectangle(length , breadth):
    area = length*breadth
    return area
# main program
length = int(input("enter the length of the rectangle:"))
breadth = int(input("enter the breadth of the rectangle: "))

result = areaOfrectangle(length, breadth)
print("Area of rectangle is area :" , result)




