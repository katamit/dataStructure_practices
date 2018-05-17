#Tree structure is also used to airthmetic expressions.
# We are goin to build up a tree for an expression written in posfix notation

# Using our earlier implemtation of stack
# --- alternatively python native list can also be used as stack
from stack import Stack


#for creating the nodes of the tree
class TreeNode:
	def __init__(self, data=None):
		self.data = data
		self.right = None
		self.left = None

#Postfix expression is split in to operator and operations
expr = "4 5 + 5 3 - *".split()


stack = Stack()

# create the tree structure
for term in expr:
	if term in '+*-/':
		node = TreeNode(term)
		node.right = stack.pop()
		node.left = stack.pop()
	else:
		node = TreeNode(int(term))
	stack.push(node)

# evaluating the expression
def calc(node):
	if node.data is '+':
		return calc(node.left) + calc(node.right)
	elif node.data is '*':
		return calc(node.left) * calc(node.right)
	elif node.data is '-':
		return calc(node.left) - calc(node.right)
	elif node.data is '/':
		return calc(node.left) / calc(node.right)
	else:
		return node.data

root = stack.pop()
result = calc(root)

print(result)