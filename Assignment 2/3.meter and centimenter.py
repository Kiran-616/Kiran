# convert distant given in feet, inches into meter and centimenter
feet = int(input("Enter distance in feet"))
inches = int(input("Enter remaining inches :"))
total_inches = (feet * 12)+ inches
centimeters = total_inches *2.54 
meters = int (centimeters // 100)
remaining_cm = round(centimeters % 100,2)
print("Distance is :",meters , "meters and ,remaining_cm","centimeters")