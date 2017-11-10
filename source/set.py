from hashtable import HashTable

class Set(object):

	def __init__(self, elements=None):
		self.items = HashTable(elements)
		self.size = 0