# Sum all the items in a dictionary
my_dict = {1:10,2:20,3:30}
total = 0

for value in my_dict.values():
    total += value
print("sum of all items:" ,total)