'''Demonstration of an iterator class that works on any collection that support both __len__ and __getiem___

python also provides an automatic iterator implementation for any class that defines both __len__ and __getitem__
which can be crated using iter()

'''
class SequenceIterator:
	"""An iterator for any of python's sequence types"""
	def __init__(self, sequence):
		# super(SequenceIterator, self).__init__()
		self._seq = sequence
		self._k = -1

	def  __next__(self):
		'''Return the next element or else raise StopIteration error'''
		self._k += 1
		if self._k <= len(self._seq):
			return self._seq[self._k]
		else:
			raise StopIteration()
		
	def __iter__(self):
		''' By Convention, an iterator must return itself as an iterator'''
		return self


def test():
	a = 2
	# iterator = SequenceIterator([2,3,2])
	iterator = SequenceIterator(a)
	print(iterator)
	print(next(iterator))
	print(next(iterator))
	print(next(iterator))
	# print(next(iterator))
	# for val in iterator:
		# print(val)


if __name__ == '__main__':
	test()