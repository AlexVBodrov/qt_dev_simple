# body = Body(name, ro, volume)

class Body():
	# где name - название тела (строка);
 	# ro - плотность тела (число: вещественное или целочисленное);
  	# volume - объем тела  (число: вещественное или целочисленное).

	def __init__(self, name, ro, volume) -> None:
		self.name = name
		self.ro = ro
		self.volume = volume
		self.weight = self.count_weight(ro, volume)

	def count_weight(self, ro, volume):
		# Масса тела вычисляется по формуле: m = ro * volume
		return ro * volume

	@classmethod
	def __verify_data(cls, other):
		if not isinstance(other, (int, Body)):
			raise TypeError("Операнд справа должен иметь тип int или Body")
		
		return other if isinstance(other, int) else other.weight

	def __gt__(self, other):
		weight_other = self.__verify_data(other)
		return self.weight > weight_other

	def __eq__(self, other):
		weight_other = self.__verify_data(other)
		return self.weight == weight_other

	def __lt__(self, other):
		weight_other = self.__verify_data(other)
		return self.weight < weight_other

	"""
	body1 > body2  # True, если масса тела body1 больше массы тела body2 # __gt__(self, other)*
	body1 == body2 # True, если масса тела body1 равна массе тела body2 # __eq__(self, other)*
	body1 < 10     # True, если масса тела body1 меньше 10 # __lt__(self, other)*
	body2 == 5     # True, если масса тела body2 равна 5 # __eq__(self, other)*
	"""
