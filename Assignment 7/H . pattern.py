n = 8
for i in range(1,6):
    for j in range(1,i+1):
        if(j!=5):
            print(j,end=" ")
    for j in range (1,n):
        print(" " ,end=" ")
    n = n-2
    for j in range(i,0,-1):
        print(j,end=" ")
    print()







    