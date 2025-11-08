mg = input("enter anu number")
lower = 0
upper = 0
for x in mg:
    if x in "abcdefghijklmnopqrstuvwxyz":
        lower+= 1
    elif x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        upper+=1
print("total upper",upper)
print("total lower",lower)


