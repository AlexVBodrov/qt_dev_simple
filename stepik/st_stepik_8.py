"""
На вход программе подаются два натуральных числа aa и bb.
Напишите программу с использованием встроенной функции all() 
для обнаружения всех целых чисел в диапазоне [a;b],
которые делятся на каждую содержащуюся в них цифру без остатка.
"""
# a, b = input(), input()
a, b = '1', '25'


def fillter_a_b(a, b):
    list_nums = list(range(int(a), int(b)+1))
    res = []
    
    for el in list_nums:
        lenth = 0
        for num in str(el):
            if num != '0' and el % int(num) == 0:
                lenth += 1
                if lenth == len(str(el)):
                    res.append(el)
            else:
                break
        
    return res


print(*fillter_a_b(a, b))


# Верное решение #439217749
# Python 3
def check(num):
    return all(map(lambda x: int(x) and num % int(x) == 0, str(num)))

a, b = int(input()), int(input())
seq = range(a, b + 1)
print(*list(filter(lambda x: check(x), seq)))

