#
#Author : amit
#Created Date : 05-May - 2018
#
'''
This program demonstrate the creation and some other functionalies like:
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
	def __init__(self, data):
		self.data = data
		self.next = None

# Implementation of the singely linked list
class SingleLinkedList:
	def __init__(self, value=None):
		self.head = None
		self.tail = None
		self.length = 0
		if value:
			node = Node(value)
			self.head = node
			self.tail = node
			self.length += 1

# Add an element to the end of the list
	def push(self, data):
		node = Node(data)
		if not self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.length += 1

# Add an element to the beginning of the list
	def push_left(self, data):
		node = Node(data)
		if not self.head:
			self.head = Node
			self.tail = Node
		else:
			node.next = self.head
			self.head = node
		self.length += 1

	def pop(self):
		# Need to iterate to pop the last element which is a over head
		# can be handle easily by putting one more prev pointer in node class as we will 
		# see in case of doubly linked list
		if not self.tail:
			return None
		
		prev = None
		current = self.head
		# checking for the list with only one element
		if self.length == 1:
			value = current.data
			self.head = None
			self.tail = None
			self.length -= 1
			return value

		while current.next:
			prev = current
			current = current.next
		value = current.data
		prev.next = None
		self.tail = prev
		self.length -= 1
		return value

# Delete a element from the left
	def pop_left(self):
		if not self.head:
			return None
		value = self.head.data
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.tail = None
		return value

# remove a  node by the value
	def remove(self, value):
		if not self.head:
			return None
		if self.head.data == value:
			if self.pop_left():
				return True

		prev = self.head
		current = self.head.next
		while current:
			if current.data == value:
				prev.next = current.next
				self.length -= 1
				if self.tail == current:
					self.tail = prev
				return True
			prev = current
			current = current.next
		else:
			return False


# return the size of the linked list
	def get_length(self):
		return self.length

# Traversing the list
	def iter(self):
		current = self.head
		while current:
			value = current.data
			current = current.next
			yield value

# search a element
	def search(self, value):
		# other way of implementation
		# if !self.head:
		# 	retrun False
		# current = self.head
		# while current:
			# if current.data == value:
			# 	return True
			# current = current.next
		# else:
		# 	return False
		for val in self.iter():
			if val == value:
				return True
		else:
			return False

# clearing a list
	def clear(self):
		self.head = None
		self.tail = None
		self.length = 0



# The function to test above created list.
def test():
	print('Creating a new single linked list with 1 as first element')
	new_list = SingleLinkedList(1)
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

	# singleElementList = SingleLinkedList(90)
	# print('Removing the LAST ITEM from the list return value must be 11')
	# print(singleElementList.pop())
	# assert singleElementList.get_length() == 0

	# print('Removing the FIRST ITEM from the list return value must be NONE')
	# print(singleElementList.pop_left())
	# assert singleElementList.get_length() == 0
	# i = 1
	# print('-'*60)
	# print('Printing the list of length %d'%singleElementList.get_length())
	# for item in singleElementList.iter():
	# 	print('index %d and value is -> %d'%(i ,item))
	# 	i += 1
	# print('-'*60)

test()
