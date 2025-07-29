def add (a, b):
    return a + b
def substract (a, b):
    return a - b
def multiply (a, b):
    return a * b
def divide (a, b):
    if b != 0:
     return a / b
    else:
       return "cannot be divided"
    
print("select the operation: add,substract,multiply,divide")
op = input("enter operations").strip().lower()
print("you enterd",op)
a = float(input("enter the first number:"))
b = float(input("enter the secound number:"))
if op == "add":
    print("result:", add(a,b))
elif op == " sub":
    print("result",substract(a,b))
elif op =="multiply":
    print("result",multiply(a,b))
elif op =="divide":
    print == ("result",divide(a,b))
else:
    print("invalid operation")
       



