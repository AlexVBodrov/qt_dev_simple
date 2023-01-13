# r = Record(field_name1=value1,... , field_nameN=valueN)

class Record:
    def __init__(self, **kwargs):
        # field_nameX - наименование поля БД; valueX - значение поля из БД.
        self.__dict__.update(kwargs)
        self.__total_attrs = len(kwargs)
        self.__attrs = tuple(self.__dict__.keys())
    
    def __check_index(self, indx):
        if type(indx) != int or not (-self.__total_attrs <= indx < self.__total_attrs):
            raise IndexError('неверный индекс поля')
    
    def __getitem__(self, item):
        self.__check_index(item)
        return getattr(self, self.__attrs[item])
    
    def __setitem__(self, key, value):
        self.__check_index(key)
        setattr(self, self.__attrs[key], value)

r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП