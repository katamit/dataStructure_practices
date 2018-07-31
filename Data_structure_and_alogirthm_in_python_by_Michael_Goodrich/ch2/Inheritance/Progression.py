''' this is the basic progression implementing the convenition of a python iteator ie.
	__iter__ and __next__

'''


class Progression:
	"""Iterator producing a generic progression 

	Default iterator produces the whole number 0 1 2 ...."""
	def __init__(self, start= 0):
		"""Initialize current to the first value of the progression"""
		self._current = start

	def _advance(self):
		"""Update self._current  to a new value
		This should be overridden by a subclass to customize progression.

		By convention, if current is set to None this designate the 
		end of a finite progression"""
		self._current += 1

	def _iter__(self):
		"""By Convention, an iterator must return itself as an interator"""
		return self

	def __next__(self):
		"""Return the next element, or else raise StopIterator error"""
		if self._current is None: # our convention ot end a progression
			raise StopIteration()

		answer = self._current
		self._advance()
		return answer


	def _print_progression(self, n):
		""" Print next n values of the progression """
		return (' '.join(str(next(self)) for j in range(n)))


def test():
	prog = Progression()

	print(prog._print_progression(10))


if __name__ == '__main__':
	test()