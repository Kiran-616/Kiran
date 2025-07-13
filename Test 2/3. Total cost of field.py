# A farmer has a field which is half in circle shape and rest rectangle
import math

radius = 20
length = 50
breadth = 40
cost_per_meter = 35
wires = 5

if radius <= 0 or length <= 0 or breadth <= 0 or cost_per_meter <= 0:
     
     print("Invalid input: Radius, length , and cost must be positive numbers.")

else:
     half_circle =( 2 * math.pi * radius / 2)
     rectangle = 2 * (length + breadth)
     total_length = (half_circle + rectangle) * wires

     total_cost = total_length * cost_per_meter
     print(" Total cost of fencing the field is Rs.", round(total_cost, 2))



