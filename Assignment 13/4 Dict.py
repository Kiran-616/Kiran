# Generate a dictionary that contance numbers between 1 and n in the form x,x*x
n = 5
result = {}

for x in range(1,n+1):
    result[x] = x*x
print("generated dictionary:" , result)