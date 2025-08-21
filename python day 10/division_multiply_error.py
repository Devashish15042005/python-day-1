try:
    number_1 = int(input("enter any number"))
    number_2 = int(input("enter any number")) 
    print("result",number_1/number_2)
except ZeroDivisionError:
 print("it cannot be divided by zero")
except ValueError:
   print("please enter a number")