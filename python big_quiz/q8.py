def get_even_num(number):
    even_lit = []
    for num in number:
        if num % 2 == 0:
            even_lit.append(num)
    return even_lit
print(get_even_num([1,2,3,4,5,6,7,8,9,10]))