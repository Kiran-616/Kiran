# Write a program to calculate the total cost of painting . The interior of building with four equal sized
height = float(input("Enter height of wall (in meters):"))
width = float(input("Enter width of wall (in meters):"))
cost_per_sq_meter = float(input("Enter paintings cost per square meter:"))

if height <= 0 or width <= 0 or cost_per_sq_meter <= 0:
    print(" Invalid input ! Height, Width, and cost must be positive values")
else:
     wall_area = height *width 
     total_area =wall_area * 4 

     total_cost = total_area * cost_per_sq_meter
     print("Total cost of paintings 4 walls is Rs.", round(total_cost, 2))
