from hashtable import HashTable

class Set(object):

	def __init__(self, elements=None):
		self.items = HashTable()
		self.size = self.items.size

		for element in elements:
			self.items.set(element, None)

	def add(self, element):
		if self.ite