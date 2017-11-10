

class Circular_Buffer(object):
	
	##### TODO: Get rid of size property. Use position of head and tail to determine if queue is empty.

	def __init__(self, max_size):
		self.items = [_ for _ in range(max_size)]

		self.size = 0 # Count of items that were enqueued
		self.head = 0
		self.tail = 0 
		self.max_size = max_size

	def enqueue(self, item):
		if self.is_full():
			raise Exception("Queue is full")

		# end_index = self.tail % self.max_size
			## Removed b/c it would calculate an index before adding initial element

		# test = end_index # Used in print statements below

		# self.items[end_index] = item
			## End index no longer needed. Can use tail.
		self.items[self.tail] = item

		self.size += 1
		# self.tail += 1
			## Instead of incrementing tail by one we can update using modulo
		self.tail = (self.tail + 1) % self.max_size

	def dequeue(self):
		if self.size == 0:
			raise Exception("Queue is empty")

		# start_index = self.head % self.max_size
			## Removed b/c it would calculate an index before adding initial element
		# item = self.items[start_index]
			## start index no longer needed. Can use head.
		item = self.items[self.head]

		# self.items[start_index] = 0
			## No need to set dequeued values to zero. They will be overwritten
		# self.head += 1
			## Instead of incrementing head by one we can update using modulo

		self.head = (self.head + 1) % self.max_size
		self.size -= 1

		return item


	def is_full(self):
		return self.size == self.max_size

if __name__ == '__main__':

	test = Circular_Buffer(5)
	print("inital_size: ", test.size)
	print("===========================intial items", test.items)
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
	test.enqueue("K")
	test.dequeue()
	test.enqueue("L")
	test.dequeue()
	test.dequeue()
	test.dequeue()
	test.dequeue()
	test.dequeue()
	print("full", test.is_full())

	# test.enqueue("J")
	# test.enqueue("F")
	# test.dequeue()

