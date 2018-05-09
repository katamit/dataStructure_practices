#
#Author : amit
#Created Date : 05-May -2018
#
'''
This program demonstrate the creation and some other functionalies of Doubly Linked List like:
	1. push
	2. push to the left
	3. pop
	4. pop from the left
	5. search an element
	6. remove a element by value
	7. get the length of the list
	8. generator to iterate over the list
	9. clear/empty a list
'''

# Represent of a single node in a list
class Node:
	def __init__(self, data=None, prev=None, next_ref=None):
		self.data = data
		self.prev = prev
		self.next = next_ref



class CircularDoublyLinkedList:
	def __init__(self,data=None):
		self.__head = None
		self.__tail = None
		# to keep the count of number of nodes in list
		self.count = 0
		if data:
			node = Node(data)
			node.prev = node
			node.next = node
			self.__head = node
			self.__tail = node
			self.__count = 1

#push the tail
	def push(self,value):
		node = Node(value, self.__tail, self.__head)
		if self.__count == 0: # not self.__tail
			node.prev = node
			node.next = node
			self.__head = node
			self.__tail = node
		else:
			self.__tail.next = node
			self.__tail = node
			self.__head.prev = self.__tail
		self.__count += 1

# push the head
	def push_left(self,value):
		node = Node(value, self.__tail, self.__head)
		if self.__count == 0: # not self.__tail
			node.prev = node
			node.next = node
			self.__head = node
			self.__tail = node
		else:
			self.__head.prev = node
			self.__head  = node
			self.__tail.next = self.__head
		self.__count += 1

# pop the tail
	def pop(self):
		if self.__count == 0:
			raise IndexError('List is Empty')
		value = self.__tail.data
		if self.__count == 1:
			self.__head = None
			self.__tail = None
		else:
			self.__tail = self.__tail.prev
			self.__tail.next = self.__head
			self.__head.prev = self.__tail
		self.__count -= 1
		return value

# pop the head
	def pop_head(self):
		if self.__count == 0:
			raise IndexError('List is Empty')
		value = self.__head.data
		if self.__count == 1:
			self.__head = None
			self.__tail = None
		else:
			self.__head = self.__head.next
			self.__head.prev = self.__tail
			self.__tail.next = self.__head
		self.__count -= 1
		return value

	def iter(self):
		if self.__count == 0 or not self.__head:
			raise IndexError('List is Empty')
		current = self.__head
		condition = True
		# while current is not None and current.next is not self.__head:
		while condition:
			value = current.data
			current = current.next
			condition = current is not self.__head
			yield value

	def search(self, value):
		# if self.__count == 0:
		# 	raise IndexError('List is Empty')
		for val in self.iter():
			if val == value:
				return True
		else:
			return False

	def get_length(self):
		return self.__count

	def remove(self, value):
		if self.__count == 0:
			raise IndexError('List is Empty')
		if self.__head.data == value:
			if self.pop_head():
				return True

		current = self.__head.next
		while current is not self.__head:
			if current.data == value:
				if current is self.__tail:
					if self.pop():
						return True
				else:	
					current.prev.next = current.next
					current.next.prev = current.prev
					self.__count -= 1
					return True
			current = current.next
		return False

	def clear(self):
		self.__head = None
		self.__tail = None
		self.__count = 0


# The function to test above created list.
def test():
	print('Creating a new doubly linked list with 1 as first element')
	new_list = CircularDoublyLinkedList(1)
	assert new_list is not None
	assert new_list.get_length() == 1

	print('-'*60)
	print('adding the element 2,4,6,8,10 to end of the list')
	new_list.push(2)
	new_list.push(4)
	new_list.push(6)
	new_list.push(8)
	new_list.push(10)
	assert new_list.get_length() == 6
	
	print('-'*60)
	print('adding the element 3,5,7,9,11 to beginning of the list')
	new_list.push_left(3)
	new_list.push_left(5)
	new_list.push_left(7)
	new_list.push_left(9)
	new_list.push_left(11)
	assert new_list.get_length() == 11
	print('-'*60)

	print('seraching the element 32 in list. Must return False')
	print(new_list.search(32))
	print('-'*60)

	print('seraching the element 2 in list. Must return True')
	print(new_list.search(2))
	assert new_list.get_length() == 11
	print('-'*60)
	print('Printing the list of length %d'%new_list.get_length())
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1
	print('-'*60)

	print('Pop the last item from the list return value must be 10')
	print(new_list.pop())
	assert new_list.get_length() == 10

	print('-'*60)
	print('Pop the first item from the list return value must be 11')
	print(new_list.pop_head())
	assert new_list.get_length() == 9
	
	print('-'*60)
	print('Printing the list of length %d'%new_list.get_length())
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1
	
	print('-'*60)
	print('Remove by value the first item')
	new_list.remove(9)
	assert new_list.get_length() == 8
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1
	
	print('-'*60)
	print('Remove by value the last item')
	new_list.remove(8)
	assert new_list.get_length() == 7
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1
	
	print('-'*60)
	print('Remove by value the any item')
	if new_list.remove(8):
		assert new_list.get_length() == 6
	else:
		assert new_list.get_length() == 7
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1

	print('-'*60)
	print('Remove by value of a repeated itme')
	new_list.push(1)
	if new_list.remove(1):
		assert new_list.get_length() == 7
	else:
		assert new_list.get_length() == 8
	i = 1
	for item in new_list.iter():
		print('index %d and value is -> %d'%(i ,item))
		i += 1

	print('-'*60)
	print('Clearing the list . Length must be 0 for the list')
	new_list.clear()
	assert new_list.get_length() == 0
	print('-'*60)



# Testing with the list of only on item
# Uncomment the below code block to test for functionalies with list of only one element

	# singleElementList = DoublyLinkedList(90)
	# print('Removing the LAST ITEM from the list return value must be 11')
	# print(singleElementList.pop())
	# assert singleElementList.get_length() == 0

	# print('Removing the FIRST ITEM from the list must raise IndexError')
	# print(singleElementList.pop_head())
	# assert singleElementList.get_length() == 0

	# print('-'*60)
	# print('Search the list')
	# singleElementList.search(10)
	
	# print('-'*60)
	# print('Printing the list of length %d'%singleElementList.get_length())
	# i = 1
	# for item in singleElementList.iter():
	# 	print('index %d and value is -> %d'%(i ,item))
	# 	i += 1
	# print('-'*60)

test()


