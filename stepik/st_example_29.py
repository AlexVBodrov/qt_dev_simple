class IntegerValue:
    # raise ValueError('возможны только целочисленные значения')
    def __set_name__(self, owner, name):
        self.name = "_" + name 

    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

class CellInteger:
    
    value = IntegerValue()
    
    def __init__(self, start_value=0):
        self.value = start_value
    

# table = TableValues(rows, cols, cell=CellInteger)

class TableValues:
    def __init__(self, rows, cols, cell=None):
        #  rows, cols - число строк и столбцов (целые числа); cell - ссылка на класс, описывающий работу с отдельными ячейками таблицы. Если параметр cell не указан, то генерировать исключение командой:
        # raise ValueError('параметр cell не указан')
        if not cell:
            raise ValueError('параметр cell не указан')
        
        self._rows = rows
        self._cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for _ in range(rows))
    
    def __check_index(self, index):
        r, c = index
        if type(r) != int or not (0 <= r < self._rows) or type(c) != int or not (0 <= c < self._cols):
            raise IndexError('IndexError')
         
    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value
    
    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value
    
    



    
    