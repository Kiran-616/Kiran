# Program to remo:ve the given key from a dictionary
my_dict = {"name": "kiran", "age":22,"city":"pune"}

key_to_remove = "age"
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
print("dictionary after removal:",my_dict)