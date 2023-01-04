# from operator import *

def arithmetic_operation(operation):
    def funtc(x, y):
        # kw = {"+" : add,
        # "-" : sub,
        # "*" : mul,
        # "/" : truediv}
        res = eval(f'{x}{operation}{y}')
        return res
    return funtc

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))