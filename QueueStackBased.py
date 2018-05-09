'''
Implementing a Queue using two stack is a popular question posed 
during interviews
'''

## Here python builtins list has been used as stack

class QueueStackBased:
	def __init__(self, data=None):
		self.inbound_stack = []
		self.outbound_stack = []
		self.size = 0
		if data:
			self.inbound_stack.append(data)
			self.size += 1


	def enque(self, value):
		self.inbound_stack.append(value)
		self.size += 1

	def deque(self):
		if not self.outbound_stack and not self.inbound_stack:
			raise IndexError('Queue is Empty')

		if not self.outbound_stack:
			while self.inbound_stack:
				self.outbound_stack.append(self.inbound_stack.pop())
		self.size -= 1

		return self.outbound_stack.pop()

	def get_size(self):
		return self.size


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
	my_queue = QueueStackBased(1)

	print('adding million items to list')
	for i in range(2, 10**6):
		my_queue.enque(i)

	print('Deque an element from my Queue')
	print(my_queue.deque())

	print('Printe the size of the Queue')
	print(my_queue.get_size())

test()