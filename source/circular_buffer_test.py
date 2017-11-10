from circular_buffer import Circular_Buffer 
import unittest

class Circular_Buffer_Test(unittest.TestCase):

	def test_init(self):
		first = Circular_Buffer(8)
		assert len(first.items) == 8
		assert first.max_size == 8

	def test_enqueue(self):
		test = Circular_Buffer(3)
		assert test.max_size == 3

		test.enqueue("A")
		assert test.items[test.head] == "A"
		test.enqueue("B")
		test.enqueue("C")
		assert test.items[test.head] == "A"
		assert test.size == 3

		with self.assertRaises(Exception):
			test.enqueue("D")

	def test_dequeue(self):
		test = Circular_Buffer(8)
		with self.assertRaises(Exception):
			test.dequeue()

		test.enqueue("A")
		test.enqueue("B")
		test.enqueue("C")
		assert test.size == 3
		test.dequeue()
		assert test.items[test.head] == "B"
		assert test.size == 2
		test.dequeue()
		assert test.items[test.head] == "C"
		assert test.size == 1

		test.dequeue()
		assert test.size == 0
		assert test.items[test.head] == 3 
		assert test.tail == 3

		assert test.is_full() == False

if __name__ == '__main__':
	unittest.main()


