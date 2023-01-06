# item = ShopItem(name, weight, price)

class ShopItem:
    def __init__(self, name, weight, price):
        # где name - название товара (строка); weight - вес товара (число: целое или вещественное); price - цена товара (число: целое или вещественное).
        self.name = name
        self.weight = weight
        self.price = price
    
    def __hash__(self) -> int:
        # __hash__() - чтобы товары с одинаковым названием (без учета регистра), весом и ценой имели бы равные хэши;
        return hash((self.name.lower(), self.weight, self.price))
    
    def __eq__(self, other):
        # - чтобы объекты с одинаковыми хэшами были равны.
        if not isinstance(other, ShopItem):
            raise TypeError('obj not ShopItem')
        return self.__hash__() == other.__hash__