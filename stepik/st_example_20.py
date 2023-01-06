class Descriptor:

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) not in (int, float) \
        or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        instance.__dict__[self.name] = value
        if len(instance.__dict__) == 3:
            a, b, c = sorted(instance.__dict__.values())
            if a + b <= c:
                raise ValueError("с указанными длинами нельзя образовать треугольник")


class Triangle:

    a = Descriptor()
    b = Descriptor()
    c = Descriptor()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        p = len(self) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**.5

    def __setattr__(self, key, value):
        if key in 'abc':
            object.__setattr__(self, key, value)