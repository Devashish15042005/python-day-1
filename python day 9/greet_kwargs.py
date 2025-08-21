def greet(**kwargs):
    if 'name' in kwargs:
        print("hello", kwargs['name'])
    else :
        print("hello guest")
greet(name = "devashish")
greet()