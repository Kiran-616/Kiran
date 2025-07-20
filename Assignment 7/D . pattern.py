n = 5
for i in range(1, n + 1):
    print(" " * (n - i) , end="")
    num = i
    for j in range(i):
        print(num, end=" ")
        num += 1
    num -= 2
    for j in range(i - 1):
        print(num, end=" ")
        num -= 1
    print()