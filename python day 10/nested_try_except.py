try:
    filename = input("Enter filename: ")
    with open(filename, "r") as file:
        try:
            a, b = map(int, file.read().split())
            print("Result:", a/b)
        except ZeroDivisionError:
            print("Error: Division by zero inside file data!")
except FileNotFoundError:
    print("Error: File not found!")
