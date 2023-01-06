class Box():
	# box = Box()

	def __init__(self) -> None:
		self.list_things = []

	def add_thing(self, obj):
		# - добавление предмета obj (объект другого класса Thing) в ящик;
		if isinstance(obj, Thing):
			self.list_things.append(obj)
		
	def get_things(self):
		#- получение списка объектов ящика.
		return self.list_things

	def __eq__(self, other: 'Box') -> bool:
		count = 0
		for b1 in self.get_things():
			for b2 in other.get_things():
				if b1.name == b2.name and b1.mass == b2.mass:
					count += 1
		if count == len(self.get_things()) and count == len(other.get_things()):
			return True
		else:
			return False


class Thing():
	# obj = Thing(name, mass)

	def __init__(self, name, mass) -> None:
		self.name = name
		self.mass = mass

	@classmethod
	def __verify_data(cls, other):
		if not isinstance(other, Thing):
			raise TypeError("Операнд справа должен иметь тип Thing")
		return other

	def __eq__(self, other):
		self.__verify_data(other)
		return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

t1 = Thing('Мел', 100)
t2 = Thing('мел', 100)

print(t1 == t2)
# res = b1 == b2 # True
print(b1 == b2)