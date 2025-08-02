# print 1 to 100 in snakes and ladder pattern
num = 1

for row in range(10):
    current_row = []

    for col in range(10):
        current_row.append(num)
        num +=1
    if row % 2 == 1:
        current_row.reverse()
    for value in current_row:
        print(f"{value:>4}" , end ="")
    print()

    