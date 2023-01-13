# ar = Array(max_length, cell)

class Array:
    #  max_length - максимальное количество элементов в массиве; cell - ссылка на класс,
    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__cell = cell
        self.__array = [self.__cell() for _ in range(self.__max_length)]
    
    def __check_key(self, index):
        if type(index) != int or not (-self.__max_length <= index < self.__max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')
            
    
    def __getitem__(self, key):
        self.__check_key(key)
        return self.__array[key].value
    
    def __setitem__(self, key, value):
        self.__check_key(key)
        self.__array[key].value = value
    
    def __repr__(self) -> str:
        return " ".join(map(str, self.__array))


class Integer:
    def __init__(self, start_value=0):
        # start_value - начальное значение ячейки (в данном случае - целое число).
        self.__value = start_value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if type(value) != int:
            raise ValueError('должно быть целое число')
        self.__value = value
    
    def __repr__(self) -> str:
        return str(self.__value)
    
    