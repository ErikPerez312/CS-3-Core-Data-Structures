#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
        # TODO: Running time: ??? Why and under what conditions?
    	# TODO: Memory usage: ??? Why and under what conditions?"""

    current_index = 0
    next_index = 1 # Set to '1' to initially have access to the second element

    # Check that all adjacent items are in order until the end of list, return early if not
    while next_index < len(items):
        current_item = items[current_index]
        next_item = items[next_index]

        if current_item != next_item and current_item > next_item:
            return False

        current_index += 1
        next_index += 1

    # 'items' contains a single element, is empty
    # or all comparisons completed w/o early return. 'items' is sorted. 
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""

    # Early return if 'items' is already sorted
    if is_sorted(items):
        return 

    current_index = 0
    next_index = 1 
    # Tracks index of the last sorted item
    end_index = len(items) 

    is_done_sorting = False

    ## TODO: Update with 'is_sorted' method ##
    while is_done_sorting is False:
        current_item = items[current_index]
        next_item = items[next_index]

        # Swap items if not in order. Do nothing if equal
        if current_item != next_item and current_item > next_item:
            items[current_index], items[next_index] = items[next_index], items[current_index]

        current_index += 1
        next_index += 1

        # Reached index of last sorted item. Repeat process from beginning of list
        if next_index == end_index:
            current_index = 0
            next_index = 1
            end_index -= 1

        # Last sorted item is the second item in list. Unnecessary to continue. Finished.
        if end_index == 1:
            is_done_sorting = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first 
    unsorted item, and repeating until all items are in sorted order."""

    # Tracks index of where sorted item should be inserted
    first_unsorted_index = 0
    # Tracks the minimum item's index
    minimum_index = first_unsorted_index

    while is_sorted(items) is False:
        minimum_item = items[first_unsorted_index]

        # Find the smallest value in list
        for index in range(first_unsorted_index, len(items)):
            if items[index] < minimum_item:
                minimum_item = items[index]
                minimum_index = index

        # Swap first unsorted item with the minimum item
        items[first_unsorted_index], items[minimum_index] = items[minimum_index], items[first_unsorted_index]
        first_unsorted_index += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""

    ## TODO: Refactor with while loop ## 
    if is_sorted(items):
        return

    # Tracks the last item in sorted 'list'
    sorted_end_index = 0

    for unsorted_index in range(1, len(items)):
        # Iterates through sorted 'list' from end to start
        for sorted_index in range(sorted_end_index, -1, -1):
            unsorted_item = items[unsorted_index]
            current_sorted_item = items[sorted_index]

            # Swap items if not in order
            if current_sorted_item > unsorted_item:
                items[sorted_index], items[unsorted_index] = items[unsorted_index], items[sorted_index]

                # Keep track of new index after swap
                unsorted_index -= 1
                continue
            else:
                # Current items are in order
                break

        # New item was sorted, update index
        sorted_end_index += 1

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    required_length = len(items1) + len(items2)

    first_list_index = 0 
    second_list_index = 0
    merged_list = []

    # Add all items from both lists to new list in sorted order
    while len(merged_list) != required_length:
    	# When all items in one of lists is added to merged_list, add all 
    	# remaining items from other list

    	item1 = items1[first_list_index]
    	item2 = items2[second_list_index]

    	if item1 < item2:
    		merged_list.append(item1)
    		first_list_index += 1
    	else:
    		merged_list.append(item2)
    		second_list_index += 1

    	if first_list_index >= len(items1):
    		remaining_items = items2[second_list_index:]
    		merged_list.extend(remaining_items)
    		break
    	if second_list_index >= len(items2):
    		remaining_items = items1[first_list_index:]
    		merged_list.extend(remaining_items)
    		break

    return merged_list



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    middle_index = len(items) // 2
    # Split items list into approximately equal halves
    first_half = items[:middle_index]
    second_half = items[middle_index:]

    # Sort each half using any other sorting algorithm
    insertion_sort(first_half)
    insertion_sort(second_half)

    # Merge sorted halves into one list in sorted order
    full_sorted_list = merge(first_half, second_half)
    return full_sorted_list


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
    	return items

    # Split items list into approximately equal halves
    middle_index = len(items) // 2
    left_half = items[:middle_index]
    right_half = items[middle_index:]

    # Sort each half by recursively calling merge sort
    left_half_sorted = merge_sort(left_half)
    right_half_sorted = merge_sort(right_half)

    # Merge sorted halves into one list in sorted order
    return merge(left_half_sorted, right_half_sorted)




def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
    # items = [4,2,12,3,9]
    # print("Start", items)
    # insertion_sort(items)

    # print("sorted", items)
    items1 = [4]
    items2 = [9,10,11,12,13]

    print("merge method", merge(items1, items2))
    items3 = [8,7,6,5,4,3,2,1,]
    print("Split Sort results", split_sort_merge(items3))
