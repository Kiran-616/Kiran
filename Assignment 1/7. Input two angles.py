# Program to input two angles from user and find third angle of the triangle
angle1 = float(input("Enter the first angle (in degress):"))
angle2 = float(input("Enter the second angle (in degrees):"))
angle3 = 180 - (angle1 + angle2)
print("The third angles of the triangle is:", angle3, "degrees")
