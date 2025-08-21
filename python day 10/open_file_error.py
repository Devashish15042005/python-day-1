try:
    f = open("example.txt","r")
    print(f.read())
except FileNotFoundError:
    print("error file not found")
finally:
    print("program finished")