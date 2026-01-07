n1 = int(input("enter any number"))
n2 = int(input("enter any number"))
n3 = int(input("enter any number"))
if n1 > n2 and n1 >n3:
    print(f"{n1} is greater")
elif n2> n1 and n2 >n3:
    print(f"{n2} is greater")
else:
    print(f"{n3}is greater")