#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index < len(array):
        if array[index] == item:
            return index

        return linear_search_recursive(array, item, index + 1)

    return None

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here

    item_found = False
    left = 0
    right = len(array) - 1

    while item_found == False:
        middle = (left + right) // 2

        if left > right:
            # Item not found
            break

        if array[middle] == item:
            item_found = True
            return middle

        if array[middle] < item:
            left = middle + 1

        elif array[middle] > item:
            right = middle - 1

    return None

    pass

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here

    if left == None and right == None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    middle_index = (left + right) // 2

    if array[middle_index] == item:
        return middle_index

    elif array[middle_index] < item:
        left_index = middle_index + 1
        return binary_search_recursive(array, item, left_index, right)

    elif array[middle_index] > item:
        right_index = middle_index - 1
        return binary_search_recursive(array, item, left, right_index)


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests










