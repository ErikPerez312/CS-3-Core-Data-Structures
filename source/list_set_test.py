from list_set import List_Set 
import unittest


class list_set_test(unittest.TestCase):

	def test_init(self):
		set_one = List_Set()
		assert set_one.items == []
		assert set_one.size == 0
		set_two = List_Set(["A", "B", "C"])
		assert set_two.items == ["A", "B", "C"]
		assert set_two.size == 3

	def test_add(self):
		set_one = List_Set()
		set_one.add("A")
		assert set_one.size == 1

		with self.assertRaises(KeyError):
			set_one.add("A")
		with self.assertRaises(ValueError):
			set_one.add(" ")  
		with self.assertRaises(ValueError):
			set_one.add("")  
		with self.assertRaises(ValueError):
			set_one.add(None)

	def test_remove(self):
		set_one = List_Set(["A", "B", "C", "F"])
		assert set_one.size == 4
		set_one.remove("F")
		assert set_one.items == ["A", "B", "C"]
		assert set_one.size == 3

		with self.assertRaises(KeyError):
			set_one.remove("T")
		with self.assertRaises(ValueError):
			set_one.remove(" ")  
		with self.assertRaises(ValueError):
			set_one.remove("")  
		with self.assertRaises(ValueError):
			set_one.remove(None)
	
	def test_contains(self):
		set_one = List_Set(["A", "B", "C", "F"])
		assert set_one.size == 4

		assert set_one.contains("") == False
		assert set_one.contains(" ") == False
		assert set_one.contains(None) == False

		assert set_one.contains("A") == True
		assert set_one.contains("F") == True

		set_one.remove("C")
		assert set_one.contains("C") == False
		assert set_one.size == 3

	def test_union(self):
		set_one = List_Set(["A", "B", "C", "F"])
		set_two = List_Set(["A", "B", "G", "D", "K"])
		assert set_one.size == 4
		assert set_two.size == 5

		union_set = set_one.union(set_two)
		assert union_set.items == ["A", "B", "C", "F", "G", "D", "K"]
		assert union_set.size == 7


	def test_intersection(self):
		set_one = List_Set(["A", "B", "C", "K", "F"])
		set_two = List_Set(["A", "B", "G", "D", "K"])
		assert set_one.size == 5
		assert set_two.size == 5

		matching_keys = set_one.intersection(set_two)
		assert matching_keys.size == 3
		assert matching_keys.items == ["A", "B", "K"]

	def test_difference(self):
		set_one = List_Set(["A", "B", "C", "K", "F"])
		set_two = List_Set(["A", "B", "G", "D", "K"])
		assert set_one.size == 5
		assert set_two.size == 5

		difference = set_one.difference(set_two)

		assert difference.size == 2
		assert difference.items == ["C", "F"]

	def test_is_subset(self):
		set_one = List_Set(["A", "B", "G"])
		set_two = List_Set(["A", "B", "G", "D", "K"])
		assert set_one.size == 3
		assert set_two.size == 5
		is_subset = set_one.is_subset(set_two)
		assert is_subset == True

		set_one = List_Set(["G", "A", "B"])
		set_two = List_Set(["A", "B", "G", "D", "K"])
		assert set_one.size == 3
		assert set_two.size == 5
		is_subset = set_one.is_subset(set_two)
		assert is_subset == True

		set_three = List_Set(["G", "F", "L", "O"])
		set_four = List_Set(["G", "F", "L"])
		is_subset_two = set_three.is_subset(set_four)
		assert is_subset_two == False

		set_five = List_Set(["T", "M", "L"])
		set_six = List_Set(["M", "L", "T"])
		is_subset_three = set_five.is_subset(set_six)
		assert is_subset_three == False

if __name__ == '__main__':
    unittest.main()




