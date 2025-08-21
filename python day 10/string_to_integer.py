string = ["abc","123","45","65","xyz","ijk"]
integer = []
for items in string:
    try:
     integer.append(int(items))
    except ValueError:
     print("skipping invalid items",items)
     print("converted list",integer)
    