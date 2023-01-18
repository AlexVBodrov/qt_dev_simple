# th = Thing(name, price)


class Thing:
    ID = 0
    def __init__(self, name, price, weight=None, dims=None, memory=None, frm=None):
        self.id = 1 + Thing.ID
        Thing.ID += 1
        self.name = name
        self.price = price
        self.weight = weight
        self.dims = dims
        self.memory = memory
        self.frm = frm
    
    def get_data(self):
        #  (id, name, price, weight, dims, memory, frm)
        return self.id, self.name, self.price, self.weight, self.dims, self.memory, self.frm

# table = Table(name, price, weight, dims)
class Table(Thing):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


# book = ElBook(name, price, memory, frm)
class ElBook(Thing):
    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm
        
        

table = Table("Круглый", 1024, 812.55, (700, 750, 700))
book = ElBook("Python ООП", 2000, 2048, 'pdf')
print(*table.get_data())
print(*book.get_data())
