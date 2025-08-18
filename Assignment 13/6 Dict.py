# Multiply all the items in a dictionary
my_dict = {1:2,2:3,3:4}
product = 1

for value in my_dict.values():
    product *= value
print("product of all items:" , product)