try:
    filename = input("enter the name of the file:")
    with open (filename) as file:
        print(file.read())
except FileNotFoundError:
 print("file not found")

