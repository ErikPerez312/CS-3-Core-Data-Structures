

class Circular_Buffer(object):

	def __init__(self, max_size):
		self.items = [_ for _ in range(max_size)]
		# self.start_index = 0
		# self.end_index = (self.tail + 1) % max_size

		self.size = 0
		self.head = 0
		self.tail = -1 
		self.max_size = max_size

	def enqueue(self, item):
		if self.is_full():
			raise Exception("Queue is full")

		end_index = (self.tail + 1) % self.max_size
		test = end_index
		self.items[end_index] = item
		self.size += 1
		self.tail += 1

		print("\n")
		print(" Item", item, "was inserted at index: ", test)

		print("current_size", self.size)
		print("head", self.head)
		print("tail", self.tail)
		print("items", self.items)

	def dequeue(self):
		if self.size == 0:
			raise Exception("Queue is empty")

		start_index = self.head % self.max_size
		item = self.items[start_index]
		self.items[start_index] = 0
		self.head += 1
		self.size -= 1

		print("\n")
		print("Dequeued", item)
		print("current_size", self.size)
		print("head", self.head)
		print("tail", self.tail)
		print("items", self.items)

		return item


	def is_full(self):
		return self.size == self.max_size


test = Circular_Buffer(5)
print("inital_size: ", test.size)
print("intial items", test.items)
print("intial head", test.head)
print("intial tail", test.tail)
test.enqueue("A")
test.enqueue("B")
test.enqueue("C")
test.enqueue("D")
test.enqueue("E")
test.dequeue()
test.enqueue("F")
test.dequeue()
test.enqueue("G")
test.dequeue()
test.enqueue("H")
test.dequeue()
test.enqueue("I")
test.dequeue()
test.enqueue("J")
test.dequeue()
# test.enqueue("J")
# test.enqueue("F")
# test.dequeue()

