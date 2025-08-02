# python program to sort the list according to the second element in sublist
n = int(input("enter number of sublist:"))

main_list =[]
print("enter elements of each sublist (2 elements each):")
for i in range(n):
    a = int(input(f"sublist {i+1} - first element:"))
    b = int(input(f"sublist {i+1} - second element:"))

    main_list.append([a,b])

sorted_list = sorted(main_list , key = lambda x : x [1])

print("original list of sublists: " , main_list)
print("sorted list (by second element) :" , sorted_list)