def is_even(num):
    return num% 2== 0
num= int(input("enter the number:"))
if is_even(num):
    print("even")
else: 
    print("odd")