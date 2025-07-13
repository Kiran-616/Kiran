# Wap to print armstrong number within a given range
start = int(input("Enter start of range:"))
end = int(input("Enter end of range:"))

print("f Armstrong numbers between {start} and {end } are:")

for num in range(start, end + 1):
    power = len(str(num))

    sum_of_powers = sum(int(digit)** power for digit in str(num))

    if num == sum_of_powers:
        print(num)
                        

