row = int(input("enter number of rows"))
for i in range (1,row + 1):
    for j in range(row -i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()