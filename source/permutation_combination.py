
def permutation(iterable):
	"""Returns list of all possible combinations of items taking order into account
	:param items: A list of items
	:type items: list or string
	"""
	# Ensure we work with a list if the input(iterable) is a string
	items = list(iterable)

	# No possible permutations with empty list
	if len(items) == 0:
		return []

	# Base case or early initial return
	if len(items) == 1:
		return [items]

	current_permutations = []

	# For each item in input(items), calculate its permutations
	for index in range(len(items)):
		current_first_item = items[index]

		# store list of all items except the item(current_first_item) we want to calculate perms for
		remaining_items = items[:index] + items[index + 1:]

		# Calculate all possible permutations with the list of remaining items 
		for perm in permutation(remaining_items):
			# store permutations of remaining items prepending the item(current_first_item) we
			# were calculating for
			current_permutations.append([current_first_item] + perm)

	return current_permutations


perm1 = permutation([1,2,3])
perm2 = permutation("123")

for item in perm1:
	print(item)
print("--")
for item in perm2:
	print(item)


def combination(k, available, used=[]):
	if k == len(used):
		yield tuple(used)
	elif len(available) == 0:
		pass 
	else:
		head = available.pop(0)
		used.append(head)

		print("Avaliabel", available[:])
		for c in combination(k, available[:], used[:]):
			print("Avalable for loop")
			yield c

		used.pop()

		print("Avaliabel---2", available[:])
		for c in combination(k, available[:], used[:]):
			print("Avaliabel in for loop---2", available[:])
			yield c 

print("comb ---")
comb1 = [c for c in combination(2, ['a','b','c'])]
for item in comb1:
	print(item)


print("slice test")
item = [1,2,3,4,5,6]

print("[:3]", item[:3])
print("[3:]", item[3:])
print("[:]", item[:])
print("[::", item[::])

