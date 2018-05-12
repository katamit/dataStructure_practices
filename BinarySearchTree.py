## A good reference is also available at 
#  https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

class Node:
	def __init__(self, data=None, left_ref=None, right_ref=None):
		self.data = data
		self.left_child = left_ref
		self.right_child = right_ref


class BinarySearchTree:
	def __init__(self, data=None):
		self.root = None
		self.count = 0
		if data:
			node = Node(data)
			self.root = node
			self.count += 1

	@staticmethod		
	def compare(value_1, value_2):
		if value_1 == value_2:
			return 0
		elif value_1 < value_2:
			return -1

		return 1

	def insert(self, value):
		node = Node(value)
		if not self.root:
			self.root = node
		else:
			current = self.root
			while current:
				if self.compare(value , current.data) in [0,-1]:
					if not current.left_child:
						current.left_child = node
						break
					else:
						current = current.left_child
				else:
					if not current.right_child:
						current.right_child = node
						break
					else:
						current = current.right_child
		self.count +=1

	def find_min(self):
		if not self.root:
			raise IndexError('Tree is Empty')
		else:
			current = self.root
			while current.left_child:
				current = current.left_child
			return current.data

	def find_max(self):
		if not self.root:
			raise IndexError('Tree is Empty')
		else:
			current = self.root
			while current.right_child:
				current = current.right_child
			return current.data

	def remove(self, value):
		if not self.root:
			raise IndexError('Tree is Empty')
		else:
			parent = None
			current = self.root
			while current:
				if self.compare( value, current.data) == 0: 
					if current.left_child is None and current.right_child is None:
						# print('got leaft node to remove')
						if self.root is current:
							print('remove the singel element')
							self.root = None
						elif self.compare(current.data, parent.data) in [0,-1]:
							parent.left_child = None
						else:
							parent.right_child = None
					elif current.left_child is None:
						# print('got node wiht left_child none to remove')
						if self.compare(current.data, parent.data) in [0,-1]:
							parent.left_child = current.right_child
						else:
							parent.right_child = current.right_child
					elif current.right_child is None:
						if self.compare(current.data, parent.data) in [0,-1]:
							parent.left_child = current.left_child
						else:
							parent.right_child = current.left_child
					else:
						# need to perfrom the inorder traversal to the next suitable node
						print('tthere are subtres on both side of the node ot be removed')
						parent_leftmost = current
						leftmost = current.right_child
						while leftmost.left_child:
							parent_leftmost = leftmost
							leftmost = leftmost.left_child

						current.data = leftmost.data

						if parent_leftmost.left_child == leftmost:
							parent_leftmost.left_child = leftmost.right_child
						else:
							parent_leftmost.right_child = leftmost.right_child
					break
				elif self.compare(value, current.data) == -1:
					parent = current
					current = current.left_child
				else:
					parent = current
					current = current.right_child
			else:
				raise ValueError('Provide value is not in Tree')

			self.count -= 1
			return True

	def search(self, value):
		current = self.root 
		while current:
			if current.data == value:
				return True
			elif self.compare(value, current.data) in [0, -1]:
				current = current.left_child
			else:
				current = current.right_child
		return False

	# Below preorder , inorder , postorder traversal 
	# represent the Depth first traversal techniques of traversing a tree.
	def inorder(self):
		if self.root:
			self.__inorder(self.root)
	
	def __inorder(self,node):
		if node is not None:
			self.__inorder(node.left_child)
			print(node.data)
			self.__inorder(node.right_child)

	def preorder(self):
		if self.root:
			self.__preorder(self.root)

	def __preorder(self, node):
		if node is not None:
			print(node.data)
			self.__preorder(node.left_child)
			self.__preorder(node.right_child)

	def postorder(self):
		if self.root:
			self.__postorder(self.root)

	def __postorder(self, node):
		if node is not None:
			self.__postorder(node.left_child)
			self.__postorder(node.right_child)
			print(node.data)




def test():
	print('******Creating the BST with root_node as 50*****')
	my_tree = BinarySearchTree(50)
	print('******addin the some nodes to the tree*****')
	my_tree.insert(5)
	my_tree.insert(20)
	my_tree.insert(16)
	my_tree.insert(13)
	my_tree.insert(7)
	my_tree.insert(20)
	my_tree.insert(48)
	my_tree.insert(23)
	my_tree.insert(37)
	my_tree.insert(67)
	my_tree.insert(78)
	my_tree.insert(73)
	my_tree.insert(72)
	my_tree.insert(98)
	my_tree.insert(65)
	my_tree.insert(23)
	my_tree.insert(19)
	my_tree.insert(77)
	my_tree.insert(49)
	my_tree.insert(8)
	my_tree.insert(20)
	my_tree.insert(16)
	my_tree.insert(13)
	my_tree.insert(2)
	my_tree.insert(7)
	my_tree.insert(20)
	my_tree.insert(48)
	my_tree.insert(23)
	my_tree.insert(37)
	my_tree.insert(67)
	my_tree.insert(78)
	my_tree.insert(73)
	my_tree.insert(72)
	my_tree.insert(98)
	my_tree.insert(65)
	my_tree.insert(23)
	my_tree.insert(19)
	my_tree.insert(77)
	my_tree.insert(49)
	my_tree.insert(87)
	my_tree.insert(32)
	my_tree.insert(66)
	my_tree.insert(57)
	my_tree.insert(87)
	my_tree.insert(32)
	my_tree.insert(66)
	my_tree.insert(57)


	print('Current size of tree is {}'.format(my_tree.count))

	print('*****Finding the minimum node in the tree*****')
	print('minimum value in tree is {}'.format(my_tree.find_min()))
	print('*****Finding the maximum node in the tree*****')
	print('maximum value in tree is {}'.format(my_tree.find_max()))

	print('-'*60)
	print('*****Printing the inorder elements of the tree*****')
	my_tree.inorder()

	print('-'*60)
	print('*****Printing the preorder elements of the tree*****')
	my_tree.preorder()

	print('-'*60)
	print('*****Printing the postorder elements of the tree*****')
	my_tree.postorder()

	print('-'*60)
	print('Remvoe the value 2', my_tree.remove(2))
	print('Current size of tree is {}'.format(my_tree.count))
	print('Remvoe the value 8', my_tree.remove(8))
	print('Remvoe the value 50', my_tree.remove(50))

	print('-'*60)
	print('*****Printing the elements of the tree*****')
	my_tree.inorder()
	print('-'*60)

test()
