def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
my_list = [5,10,15,20,25,30]
result = sum_of_list(my_list)
print("the total sum is result",result)