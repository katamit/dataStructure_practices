

class Node():
	def __init__(self , data=None, prev=None, next_ref=None):
		self.data = data
		self.prev = prev
		self.next = next_ref

class QueueNodeBased:
	def __init__(self, data=None):
		self.head =  None
		self.tail = None
		self.count = 0
		if data:
			node = Node(data)
			self.head = node
			self.tail = node
			self.count += 1

	def enque(self, value):
		node = Node(value, self.tail, None)
		if  self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.count += 1

	def deque(self):
		if self.head == None:
			raise IndexError('Queue is Empty')
		else:
			value = self.head.data
			self.head = self.head.next
			self.count -= 1
			return value

	def get_size(self):
		return self.count


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
	my_queue = QueueNodeBased(1)

	print('adding million items to list')
	for i in range(2, 10**6):
		my_queue.enque(i)

	print('Deque an element from my Queue')
	print(my_queue.deque())

	print('Printe the size of the Queue')
	print(my_queue.get_size())

test()

