emp = ['a','b','b','b','a','c','a','x','y','x','z']
sale=[10,20,30,20,20,20,30,10,20,30,40]
d = {}
for i in range (len(emp)):
    if emp[i] not in d.keys():
        d[emp[i]] = [sale[i]]
    else:
        d[emp[i]] = d[emp[i]]+[sale[i]]
print(d)
for a in d:
    print("emp",a,'total',sum(d[a]),"max:",max(d[a]),"min:",min(d[a]),"count",len(d[a]))