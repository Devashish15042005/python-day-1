while True:
    try:
        num = int(input("enter any number:"))
        print("you entered",num)
        break
    except ValueError:
        print("Invalid input! Enter an integer")