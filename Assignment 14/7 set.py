# Missing numbers from each set
set1 = {1,2,3,4}
set2 = {3,4,5,6}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("missing in set2:" , missing_in_set2)
print("missing in set1:" , missing_in_set1)