numbers =[i for i in range(1,1001) if any(i%d==0 for d in range(1,10))]
print(numbers)