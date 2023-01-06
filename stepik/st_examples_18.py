# bs = BookStudy(name, author, year)

class BookStudy:
    # bs = BookStudy(name, author, year)
    def __init__(self, name, author, year) -> None:
        # name - название пособия (строка);
        # author - автор пособия (строка);
        # year - год издания (целое число).
        self.name = name
        self.author = author
        self.year = year
    
    def __hash__(self):
        # хэш по : name и author (без учета регистра).
        return hash((self.name.lower(), self.author.lower()))
    
    # def __repr__(self) -> str:
    #     return f"Book: name={self.name}, author={self.author}, year={self.year};"
    
"""
Интересный факт. Выходит если в классе  определен метод __eq__ которые сравнивает hash переданных в него объектов,
тогда в set() можно передать список lst_bs с самими объектами, и set() сравнит их по hash с помощью __eq__. 
В другом случае, если метод __eq__ не определен, то в сет нужно передавать именно hash объектов списка lst_bs
"""

lst_in = [
    'Python; Балакирев С.М.; 2020',
    'Python ООП; Балакирев С.М.; 2021',
    'Python ООП; Балакирев С.М.; 2022',
    'Python; Балакирев С.М.; 2021',
]
# Сформировать список lst_bs 
lst_bs = list(map(lambda x: BookStudy(*x.split('; ')), lst_in))
lst_bs_hash = list(map(lambda x: hash(x), lst_bs))
unique_books = len(set(lst_bs_hash))
print(unique_books)


