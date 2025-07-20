for i in range(1,6):
    for j in range(i,6):
        if(j==i or j==5 or i==1):
            print(j,end=" ")
        else:
            print(" " ,end=" ")
    print()