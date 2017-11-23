
from permutation_combination import permutation, combination
import unittest
import itertools

class Permutation_Combination_Test(unittest.TestCase):

	def test_permutation(self):
		items1 = permutation([1,2,3])
		items2 = permutation(["A", "B", "C"])
		items3 = permutation([1,2,3,4,5,6,7])
		default1 = [x for x in itertools.permutations([1,2,3])]

		assert len(items1) == 6
		assert len(items2) == 6
		assert len(items3) == 5040

	def test_combination(self):
		items = combination([1,2,3])
		items2 = combination(["A", "B", "C"])
		items3 = permutation([1,2,3,4,5,6,7])
		
		assert len(items) == 3
		assert len(items2) == 3
		assert len(items3) == 2520