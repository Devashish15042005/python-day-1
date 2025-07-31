def same(list_1,list_2):
    result = []
    for item in list_1:
        if item in list_2 and item not in result:
            result.append(item)
    return result
print (same([1,2,3,4],[3,4,5,6]))
