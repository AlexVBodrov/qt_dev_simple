is_non_negative_num = lambda x: f_1(x)

def f_1(x):
    count_dot = 0
    for el in x:
        if el in '01234567890':
            continue
        elif el in '.':
            count_dot += 1
            if count_dot == 2:
                return False
        elif el == '-':
            if el in x[1:]:
                return False
            else:
                continue
        else:
            return False
    return True

def f_2(x):
    if x[0] != '-':
        return True

"""
лямбда с двумя условиями:
все символы из набора '.0123456789'
количество точек - меньше двух
"""

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))