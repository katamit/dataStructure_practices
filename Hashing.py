
## the demonstration of Hashing functionalities,
# assuming the key to be stirng

class HashItem():
	"""This represent one single item in the hashtable"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		

class HashTable(object):
	"""This class represent our HashTable
	size of the hash table has been taken to 256 item currently"""
	def __init__(self, ):
		# super(HashTable, self).__init__()
		self.size = 256
		self.slots = [None for i in range(self.size)]
		self.count = 0

	def _hash(self, key):
		"""It is assumed that key will of type string only and this hash is
		base on this assumption"""
		mult =1
		hv = 0
		for ch in key:
			hv += mult*ord(ch)
			mult += 1
		return hv % self.size

	def put(self, key, value):
		"""
		we are going to resolve the collision  by adding one to the previos hash value we
		had and getting the remainder dividing  this value by the size of the hash table.

		This is a linear way of resolving collision
		"""
		item = HashItem(key, value)
		h = self._hash(key)

		while self.slots[h] is not None:
			if self.slots[h].key == key:
				break
			h = (h+1) % self.size

		if self.slots[h] is None:
			self.count += 1
		self.slots[h] = item


	def get(self, key):
		h = self._hash(key)

		while  self.slots[h] is not None:
			if self.slots[h].key == key:
				return self.slots[h].value
			h = (h+1) % self.size

		return None

	def  __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.put(key, value)



def test():
	ht = HashTable()
	ht['good']= 'eggs'
	ht['better']= 'ham'
	ht['best']= 'spam'

	# for these the collision of has will occur and will be resolve using linear
	ht['ad`']= 'do not'
	ht['ga']= 'collide'

	for key in ['good', 'better', 'best', 'worst', 'ad`','ga']:
		print(ht[key])


test()