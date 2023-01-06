class Dimensions:
    # d = Dimensions(a, b, c)
    def __init__(self, a, b, c):
        # где a, b, c - положительные числа (целые или вещественные), описывающие габариты некоторого тела: высота, ширина и глубина.
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if not (isinstance(value, (int, float))) or value <= 0:
            raise ValueError('габаритные размеры должны быть положительными числами')
        return object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))
    
    def __repr__(self):
        return f"{self.a}x{self.b}x{self.c}"
 
s_inp = "1 -2 3; 4 5 6.78; 1 2 3; 3 1 2.5"

test_lst = [x.split() for x in s_inp.split(';')]
for i in range(len(test_lst)):
    test_lst[i] = list(map(lambda x: float(x) if '.' in x else int(x), test_lst[i]))


lst_dims = sorted([Dimensions(i[0], i[1], i[2]) for i in test_lst], key=hash)
d1 = Dimensions(1, -2, 3)
print(d1)