#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

LETTERS = string.ascii_letters

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here

    ##Method 1:
    lowercase_text = text.lower()
    left = 0
    right = len(lowercase_text) - 1

    print(LETTERS)
    while left < right:
        ##TODO: Fails two test
        # current_left_character = lowercase_text[left]
        # current_right_character = lowercase_text[right]

        if lowercase_text[left] not in LETTERS:
            left += 1
            continue

        if lowercase_text[right] not in LETTERS:
            right -= 1
            continue

        if lowercase_text[left] is not lowercase_text[right]:
            return False

        left += 1
        right -= 1

    return True
    ##Method 2:
    # S/O Stack Overflow for Regex. Link: https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
    # text = re.sub(r'\W+', '', text).lower()

    # left = 0
    # right = len(text) - 1

    # while left < right:
    #     if text[left] is not text[right]:
    #         return False

    #     left += 1
    #     right -= 1

    # return True

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    lowercase_text = text.lower()

    if left == None and right == None:
        left = 0
        right = len(text) - 1

    if left <= right:
        if lowercase_text[left] not in LETTERS:
            left_index = left + 1
            return is_palindrome_recursive(text, left_index, right)

        if lowercase_text[right] not in LETTERS:
            right_index = right - 1
            return is_palindrome_recursive(text, left, right_index)

        if lowercase_text[left] is not lowercase_text[right]:
            return False

        return is_palindrome_recursive(text, left + 1, right - 1)

    return True

    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
