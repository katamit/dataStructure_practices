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
	def __init__(self, data=None, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next

class DoublyLinkedList:
	def __init__(self, data=None):
		self.head = None
		self.tail = None
		self.count = 0
		if data:
			node = Node(data)
			self.head = node
			self.tail = node
			self.count = 1

	def push(self, data):
		node = Node(data, prev= self.tail)
		if not self.tail:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.count += 1

	def push_left(self, data):
		node = Node(data, next=self.head)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.head.prev = node
			self.head = node
		self.count += 1

	def pop(self):
		if self.count == 0:
			raise AssertionError('List is Empty')

		value = self.tail.data
		# self.tail.prev.next = None
		if self.count == 1:
			self.tail = None
			self.head = None
		else:
			self.tail = self.tail.prev
			self.tail.next = None
		self.count -= 1
		return value
	
	def pop_left(self):
		if self.count == 0:
			raise AssertionError('List is Empty')
		value = self.head.data
		if self.count == 1:
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
		self.count -= 1
		return value

	def iter(self):
		current = self.head
		while current:
			value = current.data
			current = current.next
			yield value

	def get_length(self):
		return self.count

	def search(self, data):
		if self.count == 0:
			raise AssertionError('List is Empty')
		for val in self.iter():
			if val == data:
				return True
		return False

	def remove(self, data):
		if self.count == 0:
			raise AssertionError('List is Empty')
		if self.head.data == data:
			if self.pop_left():
				return True

		# prev = self.head
		current = self.head.next
		while current:
			if current.data == data:
				if current == self.tail:
					current.prev.next = None
					self.tail = current.prev
				else:	
					current.prev.next = current.next
					current.next.prev = current.prev

				self.count -= 1
				return True
			current = current.next
		return False

	def clear(self):
		self.head = None
		self.tail = None
		self.count = 0


# The function to test above created list.
def test():
	print('Creating a new doubly linked list with 1 as first element')
	new_list = DoublyLinkedList(1)
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
	print(new_list.pop_left())
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
	assert new_list.head == None
	assert new_list.tail == None
	print('-'*60)



# Testing with the list of only on item
# Uncomment the below code block to test for functionalies with list of only one element

	# singleElementList = DoublyLinkedList(90)
	# print('Removing the LAST ITEM from the list return value must be 11')
	# print(singleElementList.pop())
	# assert singleElementList.get_length() == 0

	# print('Removing the FIRST ITEM from the list must raise AssertionError')
	# print(singleElementList.pop_left())
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









