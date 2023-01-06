
class Record:
    COUNTER_PK = 0
    # record = Record(fio, descr, old)
    def __init__(self, fio, descr, old):

        # где fio - ФИО некоторого человека (строка); descr - характеристика человека (строка); old - возраст человека (целое число).
        # pk - уникальный идентификатор записи (число: целое, положительное); формируется автоматически при создании каждого нового объекта;
        self.pk = self.__auto_count_pk()
        self.descr = descr
        self.old = old
        self.fio = fio
    
    @classmethod
    def __auto_count_pk(cls):
        result_pk = cls.COUNTER_PK + 1
        cls.COUNTER_PK = result_pk
        return result_pk
    
    def __hash__(self):
        # хэш по атрибутам: fio и old (без учета регистра)
        return (self.fio.lower(), self.old.lower())
    
    def __eq__(self, other: 'Record') -> bool:
        # для объектов класса Record  с одинаковыми хэшами оператор == должен выдавать значение True
        if not isinstance(other, Record):
            raise TypeError('not a Record')
        return hash(self) == hash(other)
    


class DataBase:
    # db = DataBase(path) где path - путь к файлу с данными БД (строка).
    def __init__(self, path):
        self.path = path
        self.dict_db = {}
    
    def write(self, record: 'Record'):
        # для добавления новой записи в БД, представленной объектом record;
        if isinstance(record, Record):
            self.dict_db[record] = []
            self.dict_db[record].append(record)
    
    def read(self, pk):
        # чтение записи из БД (возвращает объект Record) по ее уникальному идентификатору pk (уникальное целое положительное число);
        # запись ищется в значениях словаря (self.dict_db)
        for k in self.dict_db.values():
            if len(k) == 1 and k[0].pk == pk:
                return k[0]
            else:
                for v in k:
                    if v.pk == pk:
                        return v
    

r1 = Record('Кузнецов Н.И.', 'разведчик-нелегал', 35)
r2 = Record('Балакирев С.М.', 'программист', 33)
print(r1.pk, r2.pk)