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
		if !self.head:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.length += 1

# Add an element to the beginning of the list
	def pushLeft(self, data):
		node = Node(data)
		if !self.head:
			self.head = Node
			self.tail = Node
		else:
			node.next = self.head
			self.head = node
		self.length += 1

	def pop(self):
		# Need to iterate to pop the last element which is a over head
		# can be handle easily by putting one more prev pointer in node class
		pass
		if !self.tail:
			return None
		prev = self.head
		current = self.head.next
		while !current.next:
			prev = current
			current = current.next
		value = current.data
		prev.next = None
		self.tail = prev
		self.length -= 1
		return value

# Delete a element from the left
	def popLeft(self):
		if !self.head:
			return None
		value = self.head.data
		self.head = self.head.next
		self.length -= 1
		return value

# return the size of the linked list
	def length(self):
		return self.length


