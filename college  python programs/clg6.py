def getadd(n1,n2):
    print("addition:",n1+n2)
def getdivide(n1,n2):
    print("divide:",n1/n2)
def calculator(n1,n2,operation):
    if operation == "+":
        getadd(n1,n2)
    elif operation == "/":
        getdivide(n1,n2)
    else:
        print("invalid operation")
calculator(10,2,"/")