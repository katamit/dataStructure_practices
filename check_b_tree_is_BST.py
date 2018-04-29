class Node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def check(node, min, max):
	if node is None:
		return True
	elif(node.data < min or node.data > max):
			return False
	return (check(node.left, min, node.data -1) or check(node.right, node.data +1, max))



root = Node(9)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(6)

print(check(root, -100, 200))
