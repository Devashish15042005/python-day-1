emp = ['a','b','b','b','a','c','a']
sale=[10,20,30,20,20,20,30]
a = 0
b = 0
c = 0
for i in range(len(emp)):
    if emp[i] == 'a':
        a = a + sale[i]
    elif emp[i] == 'b':
        b = b + sale[i]
    elif emp[i] == 'c':
        c = c + sale[i]
    print (a,b,c)

    