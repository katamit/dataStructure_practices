"""
In stactically type languages such as java and c++, an abstract lass serves as a formal type that may guarantee
one or more abstract methods. This provides support for <polymorphism>,  as a variable may have an abstract class
as its declared type, even though it referes to an instance of a concrete subclass. Because there are no declared
types in python, this kind of plymorphism can be accomplished without the need for a unifying abstract base 
class. For this reason there is not as strong a tradition of defining abstract base class in python, although
python's abc module provides support for defining a formal abstract base class.

"""


from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
	"""Our own versio of collections.Sequence abstract base class."""

	@abstractmethod
	def __len__(self):
		"""Return the length of the sequence"""

	@abstractmethod
	def __getitem(self):
		"""Return the element at index j of the sequence"""

	def __contains(self, val):
		"""Returns True if val found in the sequence; False otherwise"""
		for j in range(len(self)):
			if self[j] == val:
				return True
		return False

	def index(self, val):
		"""Retrun leftmose index at which val is found(or raise ValueError)"""
		for j in range(len(self)):
			if self[j] == val:
				return j
		raise ValueError('value not in sequence')

	def count(self, val):
		"""Return the number of elements equal to given value"""
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k

#--------------------------------------------------------------------------------------------

def test():
	sq = Sequence()
	print(sq.count, 10)

if __name__ == '__main__':
	test()