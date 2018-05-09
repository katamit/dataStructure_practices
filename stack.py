class Node:
	def __init__(self, data=None , next_ref=None):
		self.data = data
		self.next = next_ref


class Stack:
	def __init__(self, data=None):
		self.__top= None
		self.__size = 0
		if data:
			node = Node(data)
			self.__top = node
			self.__size = 1 

	def push(self, data):
		node = Node(data,self.__top)
		self.__top = node
		self.__size += 1

	def pop(self):
		if self.__top:
			value = self.__top.data
			self.__top = self.__top.next
			self.__size -= 1
			return value
		else:
			raise IndexError('Stack is Empty')

	def peek(self):
		return self._Stack__top

	def search(self, value):
		# current = self.__top
		# while current:
		# 	if current.data == value:
		# 		return True
		# 	current = current.next
		# return False
		for data in self.iter():
			if data == value:
				return True
		return False

	def get_size(self):
		return self.__size

	def iter(self):
		current = self.__top
		while current:
			value = current.data
			current = current.next
			yield value

	def clear(self):
		self.__top = None
		self.__size = 0

def test():
	print('Creating a Empty with first value as 1')
	my_stack  = Stack(1)
	print('Adding vlaue 2 3 4 5 6 7 respectively to my_stack')
	my_stack.push(2)
	my_stack.push(3)
	my_stack.push(4)
	my_stack.push(5)
	my_stack.push(6)
	my_stack.push(7)
	assert my_stack.get_size() == 7

	print('-'*60)
	print('print the stack from top to bottom with top being considered as index 1')
	i = 0
	for value in my_stack.iter():
		i +=1
		print('Index is %d and value is -> %d'%(i,value))

	
	print('-'*60)
	print('Performing the pop opeartion over the stack')
	print(my_stack.pop())
	assert my_stack.get_size() == 6
	
	print('-'*60)
	print('RE-print the stack after one pop operation, with top being considered as index 1')
	i = 0
	for value in my_stack.iter():
		i +=1
		print('Index is %d and value is -> %d'%(i,value))	

	print('-'*60)
	print('search a value or to check the presence of a element in stack')
	print(my_stack.search(5))
	assert my_stack.search(5)
	assert not my_stack.search(15)

	print('-'*60)
	print('Get the size/length / number of element in a stack')
	print(my_stack.get_size())
	assert my_stack.get_size() == 6

	print('-'*60)
	print('Clear the stack')
	my_stack.clear()
	# assert my_stack._Stack__top is None
	assert my_stack.get_size() == 0

	# Must return our Assert Error of stack is Empty
	# print(my_stack.pop())


test()