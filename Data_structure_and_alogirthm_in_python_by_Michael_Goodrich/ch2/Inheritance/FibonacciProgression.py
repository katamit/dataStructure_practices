
from Progression import Progression

class FibonacciProgression(Progression):
	"""Iterator Producing a generalized Fibonacci progression"""
	def __init__(self, first =0, second = 1):
		"""Create a new Fibonacci progression
		first   the first term of the progression (default 0)

		second  the second term of the progression (default 1)
		"""
		super(FibonacciProgression, self).__init__(first) #start progression at first
		# super().__init__(first)
		self._prev = second -first #fictious vlaue preceding the first

	def _advance(self):
		"""Update current value by taking the sum of previous two"""
		self._prev , self._current = self._current, self._prev + self._current

def test():
	geo_p = FibonacciProgression()
	print(geo_p._print_progression(10))

	
		
if __name__ == '__main__':
	test()