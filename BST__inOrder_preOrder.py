class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, value):
		if self is None:
			return Node(value)
		elif self.data == value:
			print('value already in data structure')
		elif value < self.data:
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)
		return self

	def preorder(self):
		if self.left is not None:
			self.left.preorder()
		print(self.data)

		if self.right is not None:
			self.right.preorder()

	def inorder(self):
		print(self.data)
		if self.left is not None:
			self.left.preorder()
		

		if self.right is not None:
			self.right.preorder()

	def postorder(self):
		if self.left is not None:
			self.left.preorder()
		
		if self.right is not None:
			self.right.preorder()
		print(self.data)
# this is idea
	def tree_sorted_in_rever(self):
		if self.right is not None:
			self.right.tree_sorted_in_rever()
		print(self.data)

		if self.left is not None:
			self.left.tree_sorted_in_rever()

	def contains(self, value):
		if self.data == value:
			return True
		elif value < self.data:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		else:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)


if __name__ == '__main__':
	root = Node(19)
	root.insert(12)
	# print(root.left.data)

	root.insert(28)
	root.insert(21)
	root.insert(17)
	root.insert(16)
	root.insert(15)
	root.insert(23)
	root.insert(40)
	root.insert(79)
	root.insert(10)
	root.insert(90)
	root.insert(80)
	# print(root.right.data)

	print(' Below is the inorder print')
	root.inorder()
	print(' Below is the preorder print which in fact print value in ascedn sort too')
	root.preorder()
	print(' Below is the postorder print')
	root.postorder()
	print(' Tree printed in sorte desc')
	root.tree_sorted_in_rever()

	#check if valu is there in tree or not
	print('check the presence fo value')
	print(root.contains(90))
	print(root.contains(100))
	print(root.contains(1))





