def my_range(start,stop=None,step=2):
    if (stop is None):
        start,stop=0,start
    if step==0:
        raise ValueError("step cannot be 0")
    if step >0:
        while(start < stop):
            yield start
            start += step

for num in my_range(2,10,2):
    print(num,end=" ")

print("\n")
for num in my_range(10,2,-2):
    print(num,end=" ")