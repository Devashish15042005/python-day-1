class InvalidageError(Exception):
    pass 
try:
    age = int(input("enter any number:"))
    if age < 0:
        raise InvalidageError("age cannot be negative")
    print("your age is :",age)
except InvalidageError :
    print("ERROR")