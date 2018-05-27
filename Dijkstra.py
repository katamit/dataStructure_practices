## this program the implementation of dijkstra algorithm one of the famous algorithm based Greedy algorithm
# design. Dijkstra aims at finding the shortest path between two nodes following a Greedy approach
# i.e taking the least cost path at every step. It doesn't always result in the best(optimal) solution

# Here we use a adjacency list to represent the graph
graph = dict()

graph['A'] = {'B':5,'D':9,'E':2}
graph['B'] = {'A':5,'C':2}
graph['C'] = {'B':2,'D':3}
graph['D'] = {'A':9,'F':2,'C':3}
graph['E'] = {'A':2,'F':3}
graph['F'] = {'E':3,'D':2}

# AND A table to keep track of the path travelled with first index correspoind to each key
# representing the shortest distance from source (in our case we will take vertex 'A' as our source)
# and second index representing the previous node traversed to reach that node
import math

# these constant to represent that 0 index is distance and 1 index in previous node
DISTANCE = 0
PREVIOUS_NODE = 1
INFINITE = math.inf

table = dict()
table = {
	'A':[INFINITE, None], # since 'A' is our source node so DISTANCE IS 0
	'B':[INFINITE, None],
	'C':[INFINITE, None],
	'D':[INFINITE, None],
	'E':[INFINITE, None],
	'F':[INFINITE, None],
}

def find_shortest_path(graph, table, origin):
	set_shortest_distance(table,origin,0)
	visited_nodes = []
	current_node = origin

	while  True:
		adjcent_nodes = graph[current_node].keys()
		unvisited_nodes = set(adjcent_nodes).difference(set(visited_nodes))

		for vertex in unvisited_nodes:
			distance_to_vertex_from_starting_node = get_shortest_distance(table, vertex)

			distance_to_current_node = get_shortest_distance(table, current_node)
			distance_to_vertex_from_current_node = get_vertex_distance(graph, current_node, vertex)
			total_distance = distance_to_current_node + distance_to_vertex_from_current_node
			if total_distance < distance_to_vertex_from_starting_node:
				set_shortest_distance(table, vertex, total_distance)
				set_previous_node(table, vertex, current_node)

		visited_nodes.append(current_node)
		if len(graph.keys()) == len(visited_nodes):
			break
		current_node = get_next_node(table, visited_nodes)

def get_shortest_distance(table, vertex):
	return table[vertex][DISTANCE]

def get_vertex_distance(graph, key, vertex):
	return graph[key][vertex]

def set_shortest_distance(table, vertex, distance):
	table[vertex][DISTANCE] = distance

def set_previous_node(table, vertex, previous_node):
	table[vertex][PREVIOUS_NODE] = previous_node

def get_next_node(table, visited_nodes):
	unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
	assumed_min = table[unvisited_nodes[0]][DISTANCE]
	min_vertex = unvisited_nodes[0]
	for vertex in unvisited_nodes:
		if table[vertex][DISTANCE] < assumed_min:
			assumed_min = table[vertex][DISTANCE]
			min_vertex = vertex
	return min_vertex


# this for testing the dijkstra algorithm
find_shortest_path(graph, table, 'A')
print(table)




