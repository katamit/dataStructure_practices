
from Progression import Progression

class GeometricProgression(Progression):
	"""Iterator Producing an geometric progression"""
	def __init__(self, base =2, start = 1):
		"""Create a new geometric progression
		base   the fixed constant multiplied to each term (default 2)

		start  the first term of the progression (default 1)
		"""
		super(GeometricProgression, self).__init__(start)
		# super().__init__(start)
		self._base = base

	def _advance(self):
		"""Update current value by multiplying it by the fixed base"""
		self._current *= self._base


def test():
	geo_p = GeometricProgression(2)
	print(geo_p._print_progression(10))
		
if __name__ == '__main__':
	test()