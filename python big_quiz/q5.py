year = int(input("enter your year"))
if (year%400 == 0) or ( year%100 != 0 and year % 4 == 0):
    print ("the year is leap year")
else:
    print("the year is not a leap year")