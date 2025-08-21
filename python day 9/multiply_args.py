def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print("product",multiply(10,20,30))