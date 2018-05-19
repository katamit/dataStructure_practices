# This file is a demonstration of 
# BFS - Breath First Search in a undirected Graph
# DFS - Depth First Search in a Directed Graph

# Let us represent the graph using a dict

graph = dict()
graph['A'] = ['B','G','D']
graph['B'] = ['A','F']
graph['C'] = ['F','H']
graph['D'] = ['F','A']
graph['E'] = ['B','G']
graph['F'] = ['B','D','C']
graph['G'] = ['A','E']
graph['H'] = ['C']

def breath_first_search(graph, root):
	'''
	In BFS in a graph the sibling are traveresed before the siblings
	we use a queue to implement the BFS here
	'''
	from collections import deque
	queue = deque([root])
	visited_nodes = [root]

	while len(queue) > 0:
		current_node = queue.popleft()
		child_nodes = graph.get(current_node)

		if child_nodes is not None:
			unvisited_nodes = set(child_nodes).difference(set(visited_nodes))
			for child in unvisited_nodes:
				queue.append(child)
				visited_nodes.append(child)
	return visited_nodes


graph2 = dict()
graph2['A'] = ['B','S']
graph2['B'] = ['A']
graph2['S'] = ['A','G','C']
graph2['D'] = ['C']
graph2['G'] = ['S','F','H']
graph2['H'] = ['G','E']
graph2['E'] = ['C','H']
graph2['F'] = ['C','G']
graph2['C'] = ['D','S','E','F']


def depth_first_search(graph,root):
	'''
	IN DFS the children of node are visited before the siblings
	Here we use Stack(list) concept to implement the stack
	'''
	visited_nodes = list()
	visited_nodes.append(root)
	graph_stack = list()
	graph_stack.append(root)

	while len(graph_stack) > 0:
		current_node = graph_stack.pop()
		child_nodes = graph.get(current_node)

		if child_nodes is not None:
			unvisited_nodes = set(child_nodes).difference(set(visited_nodes))
			for child in sorted(unvisited_nodes):
				graph_stack.append(child)
				visited_nodes.append(child)
	return visited_nodes


def test():
	print('Testing the Breadth First Search')
	print(breath_first_search(graph, 'A'))

	print('Testing the Depth First Search')
	print(depth_first_search(graph2, 'A'))


test()	