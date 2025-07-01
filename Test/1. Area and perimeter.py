# find the area and perimeter accept length, breadth, radius from user
length = int (input ("Enter the length of the rectangle:"))
breadth = int (input ("Enter the breadth of the rectangle:"))
radius = int (input("Enter the radius of the circle:"))

pi = 3.14
area_rectangle = length * breadth * radius
area_semi_circle = 0.5 * pi * radius * radius
total_area = area_rectangle + area_semi_circle

perimeter = length + 2 * breadth + pi * radius

print("\n--- combined shape ---")
print("Total area =", total_area)
print("Total perimeter = " , perimeter)

      




