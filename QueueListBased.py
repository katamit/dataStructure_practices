

class QueueListBased:
	def __init__(self, data=None):

		self.__item = []
		self.__size = 0
		if data:
			self.__item.insert(0, data)
			self.__size += 1

# Add to a list
	def enque(self, data):
		self.__item.append(data)
		self.__size += 1

# Remove from a list
	def deque(self):
		'''
		We can say the deque operation is highly inefficient. the method has to shift all the elements by one 
		after ever opeation 
		'''
		if self.__item:
			self.__size -= 1
			return self.__item.pop(0)
		else:
			raise IndexError('Queue is Empty')

# check the number of element in Queue
	def get_size(self):
		return self.__size

	def iter(self):
		for item in self.__item:
			yield item

	def search(self, value):
		for item in self.__item:
			if value == item:
				return True
		return False



# Below code is to test above written functionalites

import math
import time
from functools import wraps

def record_time(func):
	@wraps(func)
	def wrapper(*args, **kargs):
		start = time.time()
		# res =  yield from func(*args, **kargs)
		res =  func(*args, **kargs)
		end = time.time()
		print("**** The taken is {} *****".format(end- start))
		return res
	return wrapper


@record_time
def test():
	print('creatin the Queue with first elemetn as 1 ')
	my_queue = QueueListBased(1)

	print('adding million items to list')
	for i in range(2, 10**6):
		my_queue.enque(i)

	print('Deque an element from my Queue')
	print(my_queue.deque())

	print('Printe the size of the Queue')
	print(my_queue.get_size())

test()