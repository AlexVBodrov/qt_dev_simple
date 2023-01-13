from random import randint


class Cell:
    # cell = Cell()
    #  класс Cell описывает состояние одной ячейки игрового поля.
    def __init__(self):
        """
            __is_mine - булево значение True/False; True - в клетке находится мина, False - мина отсутствует;
            __number - число мин вокруг клетки (целое число от 0 до 8);
            __is_open - флаг того, открыта клетка или закрыта: True - открыта; False - закрыта.
        """
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False 
    
    """
        В этих свойствах(ниже) необходимо выполнять проверку на корректность переданных значений (либо булево значение True/False, либо целое число от 0 до 8). Если передаваемое значение некорректно, то генерировать исключение командой:
        raise ValueError("недопустимое значение атрибута")
    """
    
    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, value):
        if type(value) == bool:
            self.__is_mine = value
        else:
            raise ValueError("недопустимое значение атрибута")
    
    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if type(value) == int and 0 <= value <=8:
            self.__number = value
        else:
            raise ValueError("недопустимое значение атрибута")

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_mine(self, value):
        if type(value) == bool:
            self.__is_open = value
        else:
            raise ValueError("недопустимое значение атрибута")
    
    def __bool__(self):
        # bool(cell) возвращает True, если клетка закрыта и False - если открыта.
        return  not self.__is_open
    

# pole = GamePole(N, M, total_mines)
class GamePole:
    __instance = None
    # так как поле в игре одно, то нужно контролировать создание только одного объекта класса GamePole (используйте паттерн Singleton)
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __del__(self):
        GamePole.__instance = None

    
    def __init__(self, N, M, total_mines) -> None:
        self._n = N
        self._m = M
        self._total_mines = total_mines
        self.__pole_cells = tuple(tuple(Cell() for _ in range(M)) for _ in range(N))
        self.init_pole()
    
    @property
    def pole(self):
        return self.__pole_cells
    
    
    
    def init_pole(self):
        #- для инициализации начального состояния игрового поля (расставляет мины и делает все клетки закрытыми);
        """
            Расстановку мин выполняйте случайным образом по игровому полю (randint модуля random). После расстановки всех total_mines мин, вычислите их количество вокруг остальных клеток (где нет мин). Область охвата - соседние (прилегающие) клетки (8 штук).
        """
        for row in self.__pole_cells:
            for x in row:
                x.is_open = False
                x.is_mine = False
            
            m = 0 # counter mines
            while m < self._total_mines:
                i = randint(0, self._n - 1)
                j = randint(0, self._m - 1)
                if self.__pole_cells[i][j].is_mine:
                    continue
                self.__pole_cells[i][j].is_mine = True
                m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._m):
                if not self.pole[x][y].is_mine:
                    mines = sum(self.pole[x + i][y + j].is_mine for i, j in indx if 0 <= x + i < self._n and 0 <= y + j < self._m)
                    self.pole[x][y].number = mines
                    
                
    
    def open_cell(self, i, j):
        # открывает ячейку с индексами (i, j); нумерация индексов начинается с нуля; метод меняет значение атрибута __is_open объекта Cell в ячейке (i, j) на True;
        """
            В методе open_cell() необходимо проверять корректность индексов (i, j). Если индексы указаны некорректно, то генерируется исключение командой:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        """
        if not 0 <= i < self._n or not 0 <= j < self._m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True
    
    def show_pole(self):
        # отображает игровое поле в консоли (как именно сделать - на ваше усмотрение, этот метод - домашнее задание).
        for row in self.pole:
            print(*map(lambda x: '#' if not x.is_open else x.number if not x.is_mine else '*', row))
        

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10

pole.show_pole()
    
        
    
        
    