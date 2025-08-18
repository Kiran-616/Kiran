# Sort employees by salary

data = [
    [101 ,"seema" , 45000],
    [340,"Rajani" , 13000],
    [210,"tannu" , 14000],
    [320, "suresh" , 35000]
]

data.sort(key=lambda x: x [2])

print("sorted employees by salary:")
for emp in data:
    print(emp)