try:
    a = int(input("enter any number:"))
    b = int(input("enter any number:"))
    op = input(" choose any operator (+ - * /):")
    if op == "+":
        print("result",a+b)
    elif op == "-":
        print("result",a-b)
    elif op == "*":
        print("result",a*b)
    elif op == "/":
        print("result",a/b)
    else:
        print("invalid input")
except ValueError:
    print("enter a number")
except ZeroDivisionError:
    print("enter a non zero number")