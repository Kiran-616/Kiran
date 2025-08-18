# Wap to print following  pattern
rows = 10
cols =  16

for i in range(rows):
    if i == 0 or i == rows - 1:
        print("*" * cols)
    else:
        print(" " * (cols-i-1) + "*")



