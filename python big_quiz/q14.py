name = input("enter your name")
result = []
index = 0
for i in name:
    if i == ' ':
        n = name.index(i)
        result.append(name[index:n])
        name = name[n+1:]
if name:
    result.append(name)
print(result[::-1])