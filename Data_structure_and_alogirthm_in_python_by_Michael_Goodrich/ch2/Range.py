''' This the demonstration of range function in python'''

class Range:
	"""A class that mimic's the built-in range class"""
	def __init__(self, start, stop=None, step=1):
		"""Initialize a Range instance 

			Semantic is similar to built-in range class
		"""
		if step == 0:
			raise ValueError('step cannot be 0')

		if stop == None:
			stop, start = start, 0  # special case of range(n)

		#calculate the effective lenght once
		self._length = max(0, (stop -start + step -1)//step) 

		# need knowledge to start and step(but not stop) to support __getitem__

		self._start = start
		self._step = step


	def __len__(self):
		"""Return number of entries in the range"""
		return self._length

	def __getitem__(self, k):
		"""Return entry at index k(using standar interpreation if negative)"""
		if k < 0:
			k += len(self) #attempt to convert negative index; depends on __len__

		if not 0 <= k < self._length:
			raise IndexError('index out of range')

		return self._start + k*self._step


#------------------------------------------------------------------------------------------
def test():
	r = Range(8, 140, 5)

	print(r)
	print(len(r))

	print(r[25])
	print(r[-1])


if __name__ == "__main__":
	test()