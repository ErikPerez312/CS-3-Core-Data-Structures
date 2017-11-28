#!python

#####IMPLEMENT find index. Others should use it.

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement contains here (iteratively and/or recursively)
    if pattern == "" or pattern == text:
        return True

def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_index here (iteratively and/or recursively)

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    result_index = []

    for i in range(text_length):
        text_index = i 

        for p in range(pattern_length):
            print(text_index, "---- text index")
            if text[text_index] == pattern[p]:
                text_index += 1
                result_index.append(i)
            else:
                result_index.clear()
                break
    
        if len(result_index) == pattern_length:
            print("success match", result_index)

    print("no possible success yet", result_index)

    # pattern_index = 0
    # position_index = None

    # for char_index, char in enumerate(text):

    #     if char != pattern[pattern_index]:
    #         position = None
    #         pattern_index = 0

    #     if char == pattern[pattern_index]:
    #         if pattern_index == 0 :
    #             position = char_index

    #         if len(pattern) - 1 <= pattern_index :
    #             break
    #         else:
    #             pattern_index += 1

    # return position

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Implement find_all_indexes here (iteratively and/or recursively)
    all_indexes = [ ]
    is_found = False 
    text_index = 0 
    pattern_index = 0

    while is_found == False:
        pass

# def indexes_in_string_iterative(text, pattern):

#     text_index = 0
#     pattern_index = 0

#     text_length = len(text)
#     pattern_length = len(pattern)

#     all_indexes = []

#     # Loop through our text characters until we reach the end
#     while text_index < text_length:
#         # If our current text character is equal to our pattern character increase the index
#         if text[text_index] == pattern[pattern_index]:
#             pattern_index += 1
#         # If our current text character is not our pattern character and if we were checking for a pattern, we want to
#         # reset the pattern and try again
#         elif pattern_index > 0:
#             pattern_index = 0
#             continue

#         # If our pattern index is equal to our pattern length then we found a match and we want to add the index of the
#         # pattern start to our indexes and reset our pattern index and keep checking
#         if pattern_index + 1 > pattern_length:
#             indexes.append(text_index - (pattern_length - 1))
#             pattern_index = 0
#             continue

#         # Go to next character
#         text_index += 1

#     # Lets return our indexes
#     return all_indexes

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    # index = find_index(text, pattern)
    # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    # print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()

    find_index("twothree", "wo")
