
from Progression import Progression

class ArithmeticProgression(Progression):
	"""Iterator Producing an arithmetic progression"""
	def __init__(self, increment =1, start = 0):
		"""Create a new arithmetic progression
		increment the fixed constant to add ot each term (default 1)

		start  the first term of the progression (default 0)
		"""
		super(ArithmeticProgression, self).__init__(start)
		# super().__init__(start)
		self._increment = increment

	def _advance(self):
		"""Update current value by adding the fixed increment"""
		self._current += self._increment


def test():
	arth_p = ArithmeticProgression(2)
	print(arth_p._print_progression(10))
		
if __name__ == '__main__':
	test()