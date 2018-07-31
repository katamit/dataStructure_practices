class Vector:
	'''Represent a vector in a multidimensional spaec.'''

	def __init__(self, d):
		''' Create d-dimensional vector of zeros'''
		self._coords = [0]*d

	def __len__(self):
		'''Returns the dimension of the vector'''
		return len(self._coords)

	def __getitem__(self,j):
		'''Return jth coordinate of vector'''
		return self._coords[j]

	def __setitem__(self, j, val):
		'''Set jth coordinate of vector to given value'''
		self._coords[j] = val

	def __add__(self, other):
		'''Return sum of two vectors'''
		if len(self) != len(other):  # relies on __len__ method
			raise ValueError('dimension must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		'''Return True if vector has same coordinates as other'''
		return self._coords == other._coords

	def __ne__(self, other):
		'''Return True if vector differ from other'''
		return not self == other # relies on existing __eq__ definition

	def __str__(self):
		'''Produce string representation of vector'''
		return '< ' + str(self._coords)[1:-1] + ' >'


def test():
	v = Vector(2)

	print(v)

	iterator = iter(v)
	print(iterator)
	print(next(iterator))
	print(next(iterator))
	# print(next(iterator))

if __name__ == '__main__':
	test()
