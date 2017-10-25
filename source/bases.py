#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

values = string.digits + string.ascii_lowercase

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    if base == 2:
        
        binary_number = []
        for state in digits:
            number = int(state)


            print(number, "=======Type: ", type(number))
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    # assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    join_numbers_as_string = lambda number_array: ''.join(str(number) for number in number_array)

    # TODO: Encode number in binary (base 2)
    if base == 2:
        ## Method: 1
        quotient = number
        remainders_list = []

        while not quotient == 0:
            remainders_list.append(quotient % 2)
            quotient /= 2

        remainders_list.reverse()
        binary_number = join_numbers_as_string(remainders_list)

        # return ' '.join(string[i:i+length] for i in xrange(0,len(string),length)
        return binary_number

        ## Method 2:
        #Stack overflow
        # return "{0:b}".format(number)
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    if base == 16:
        quotient = number
        # hex_values_dict = {"0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", 
                            # "10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F", }
        remainders_list = []

        while not quotient == 0:
            remainders_list.append(quotient % 16)
            quotient /= 16

        remainders_list.reverse()

        for index, number in enumerate(remainders_list):
            remainders_list[index] = values[int(number)]

        return join_numbers_as_string(remainders_list)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    quotient = number
    remainders_list = []

    while not quotient == 0:
        remainders_list.append(quotient % base)
        quotient /= base

    for index, number in enumerate(remainders_list):
            remainders_list[index] = string.hexdigits[int(number)]

    remainders_list.reverse()
    return join_numbers_as_string(remainders_list)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()

    # number = "0010"
    # decode(number, 2)
    # fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
    # odd_numbers = filter(lambda x: x % 2 == 0, fibonacci)
    # print(odd_numbers)

    number = 5
    encode = encode(number, 10)
    print(encode)
    print(string.digits + string.ascii_lowercase)
    # print(string.hexdigits[13])

    # [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]








