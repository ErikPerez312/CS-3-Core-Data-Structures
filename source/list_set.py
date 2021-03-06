

class List_Set(object):

	def __init__(self, elements=None):
		"""initialize a new empty set structure, and add each element if a sequence is given"""
		self.items = []
		self.size = 0 # Tracks the number of elements in constant time

		if elements is not None:
			for element in elements:
				self.add(element)

	def add(self, element):
		"""add `element` to this set, if not present already"""
		if element == "" or element is None:
			raise ValueError("Element can not be None or whitespace")

		if self.contains(element):
			raise KeyError("Element already exists")

		self.size += 1
		self.items.append(element)

	def remove(self, element):
		"""remove `element` from this set, if present, or else raise `KeyError`"""
		if element == "" or element is None:
			raise ValueError("Element can not be None or whitespace")

		if self.contains(element):
			self.items.remove(element)
			self.size -= 1
		else:
			raise KeyError("Element doesn't exist in set")	

	def contains(self, element):
		"""return a boolean indicating whether `element` is in this set"""
		if element == "" or element is None:
			return False

		for item in self.items:
			if item == element:
				return True

		return False

	def union(self, other_set):
		"""return a new set that is the union of this set and `other_set`"""
		combined_elements = List_Set(self.items)
		# combined_elements = list(self.items)

		for element in other_set.items:
			if combined_elements.contains(element) == False:
				combined_elements.add(element)

		return combined_elements

	def intersection(self, other_set):
		"""return a new set that is the intersection of this set and `other_set`"""
		matching_elements = List_Set()

		for element in other_set.items:
			if self.contains(element):
				matching_elements.add(element)
			

		return matching_elements

	def difference(self, other_set):
		"""return a new set that is the difference of this set and `other_set`"""
		difference_elements = List_Set()

		for element in self.items:
			if other_set.contains(element) == False:
				difference_elements.add(element)

		return difference_elements

	def is_subset(self, other_set):
		"""return a boolean indicating whether `other_set` is a subset of this set"""
		matched_elements_count = 0

		for element in self.items:
			if other_set.contains(element):
				matched_elements_count += 1
				continue 
			else: 
				return False
		## Might not need anymore
		if matched_elements_count == self.size and matched_elements_count <= other_set.size:
			return True
		else:
			return False



if __name__ == '__main__':
    test_set = List_Set()
    print("Initial set size", test_set.size)

    print("\n Adding Value===")
    test_set.add("A")
    print("Added 'A' value. Updated size = : ", test_set.size)
    print("items : ", test_set.items)

    test_set.add("B")
    print("Added 'B' value. Updated size = : ", test_set.size)
    print("items : ", test_set.items)

    test_set.add("C")
    print("Added 'C' value. Updated size = : ", test_set.size)
    print("items : ", test_set.items)

    print("\n Removing Value ===")
    test_set.remove("C")
    print("Removed 'C' value. Updated size = : ", test_set.size)
    print("items : ", test_set.items)
    print("Removing 'Z' Key Error test", test_set.remove("z"))

    print("\nContains ====")
    print("True contains test: ", test_set.contains("A"))
    print("False contains test: ", test_set.contains("Z"))

    print("\nTesting UNION===")
    set_a = List_Set(["A", "B", "C", "D"])
    print("Set A :", set_a.items)
    set_b = List_Set(["A", "B", "C", "D", "E", "F", "G"])
    print("Set B :", set_b.items)

    union = set_a.union(set_b)
    print("set_a union set_b test:", union)


    print("\nTesting INTERSECTION===")
    set_a = List_Set(["A", "B", "C", "D", "L" , "M"])
    print("Set A :", set_a.items)
    set_b = List_Set(["A", "B", "C", "D", "E", "F", "G"])
    print("Set B :", set_b.items)

    intersection = set_a.intersection(set_b)
    print("set_a intersection set_b test:", intersection)


    print("\nTesting DIFFERENCE===")
    set_a = List_Set(["A", "B", "C", "D", "L" , "M"])
    print("Set A :", set_a.items)
    set_b = List_Set(["A", "B", "C", "D", "E", "F", "G"])
    print("Set B :", set_b.items)

    difference = set_a.difference(set_b)
    print("set_a difference set_b test:", difference)


    print("\nTesting SUBSET===")
    set_a = List_Set(["A", "B", "C", "D", "G"])
    print("Set A :", set_a.items)
    set_b = List_Set(["A", "B", "C", "D", "E", "F", "G"])
    print("Set B :", set_b.items)

    is_subset = set_a.is_subset(set_b)
    print("set_a is_subset set_b TRUE test:", is_subset)
    print("\n")
    set_a = List_Set(["A", "B", "C", "D", "G", "K"])
    print("Set A :", set_a.items)
    set_b = List_Set(["A", "B", "C", "D", "E", "F", "G"])
    print("Set B :", set_b.items)

    is_subset = set_a.is_subset(set_b)
    print("set_a is_subset set_b FALSE test:", is_subset)

