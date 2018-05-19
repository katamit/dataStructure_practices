# This file demonstrate the implementation of Heap in pyhton using the 
# python  list, 

'''
A Heap is a data structure whic satisfies the heap property. the Heap property
states that there must be  certain relationship between a parent node and its child 
node. The property must apply through the entire heap

In a MIN HEAP the relationship between parent and children is that the parent must always
be less than or equal to its children. As a consequence ot this, the lowest element in 
the heap must be the root node

In a MAX HEAP, The parent is greate than or equal to its child or its children. It 
follows from this that the largest value makes up the root node
'''

#for the sake of simpliciyt of calculat of parent and child node the 
# the 0th index of list has been filled with zero. 
class Heap:
	def __init__(self):
		self.heap = [0]
		self.count = 0
	
	def _float(self, index):
		'''
		Makes sure the min Heap is maintained by moving up the recently
		added value up the heap structure , till when its parent is less than its
		children
		'''
		k = index

		while k//2 > 0:
			# checks if the parent is greater than the child
			if self.heap[k//2] > self.heap[k]:
				self.heap[k//2], self.heap[k] = self.heap[k] ,self.heap[k//2]
			else:
				break
			k = k//2

	def insert(self, value):
		self.heap.append(value)
		self.count += 1
		self._float(self.count)


	def _min(self, k):
		if k*2 +1 > self.count:
			return k*2
		elif self.heap[k*2] < self.heap[k*2 +1]:
			return k*2
		else:
			return k*2 +1

	def _sink(self):
		k = 1
		while k*2 <= self.count:
			min_index = self._min(k)

			if self.heap[k] > self.heap[min_index]:
				self.heap[k] , self.heap[min_index]  = self.heap[min_index], self.heap[k]
			else:
				break
			k = min_index


	def pop(self):
		'''
		Pop on a min heap always return the smalles value in the heap
		in our case it will at '1' index of the heap. After that heap
		needs to be re-balanced to maintain its min heap structure.
		'''
		value = self.heap[1]
		self.heap[1] = self.heap[self.count]
		self.count -= 1
		self.heap.pop()
		self._sink()
		return value


def test():
	h = Heap()
	for i in (4,8,7,2,9,10,5,1,3,6):
		h.insert(i)
	print(h.heap)

	while len(h.heap)>1:
		n = h.pop()
		print(n)
		print(h.heap)

test()