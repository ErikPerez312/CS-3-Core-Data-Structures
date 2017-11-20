#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""

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
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of 8 or 16 items in arbitrary order
    # items = [3, 5, 4, 2, 6, 8, 1, 7]
    # items = [11, 13, 8, 4, 12, 2, 14, 3, 5, 18, 6, 10, 1, 7, 9, 15]

    # Create a list of items randomly sampled from range [1...max_value]
    import random
    items = random.sample(range(1, max_value + 1), num_items)
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    print('Initial items: {!r}'.format(items))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        sort = globals()[sort_name]
    else:
        sort = bubble_sort

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
    except:
        print('Integer required for `num` and `max` command-line arguments')

    # Test sort function, but don't explode if sort function does not exist
    try:
        test_sorting(sort, num_items, max_value)
    except NameError:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('\trandomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')


if __name__ == '__main__':
    main()
