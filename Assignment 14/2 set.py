# Remove the intersections of a second set with a first set
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
set1 -= set1 & set2

print("after removing intersection from set1:" , set1)