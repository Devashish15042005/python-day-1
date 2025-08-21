try:
 numerator = int(input("enter any number"))
 denominator = int(input("enter any number"))
 devision = numerator/denominator
except ZeroDivisionError:
 print("this cannot be devided by 0! idiot.")
