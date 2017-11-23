#!python

from math import floor, pow
import string
import unittest
import pdb

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def GET_POSSIBLE_VALUES_FOR(method):
	"""Returns helper dictionary for encode or decode methods.
	encode- Key: 1-36 Integer, Value: 1-9a-z String 
	decode- Key: 1-9a-z String, Value: 1-36 Integer
	"""
	ascii_values = string.digits + string.ascii_lowercase
	decode_values = {}
	encode_values = {}

	for index, value in enumerate(ascii_values):
		decode_values[value] = index
		encode_values[index] = value

	if method == "decode":
		return decode_values
	elif method == "encode":
		return encode_values

	raise KeyError("Method must be 'encode' or 'decode'")


DECODE_VALUES = GET_POSSIBLE_VALUES_FOR("decode")
ENCODE_VALUES = GET_POSSIBLE_VALUES_FOR("encode")


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    number_of_digits = len(digits)
    base_ten_value = 0

    for digit in digits:
        number = DECODE_VALUES[digit]
        number_of_digits -= 1

        base_ten_value += number * int(pow(base, number_of_digits))

    return base_ten_value

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    # assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    remainders_list = []
    encoded_string = str()

    while number != 0:
    	remainder = number % base 
    	number = number // base 

    	remainders_list.append(remainder)

    for item in reversed(remainders_list):
    	encoded_string += ENCODE_VALUES[item]

    return encoded_string


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    # Convert to decimal(base 10) first
    base_ten_conversion = decode(digits, base1)
    return encode(base_ten_conversion, base2)


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
	# print(convert("124", 8, 10))

	# for key, value in DECODE_VALUES.iteritems():
	# 	print("key", key, "value: ", value)

	# print("=========")
	for key, value in ENCODE_VALUES.iteritems():
		print("key", key, "value: ", value)

    # main()

	print(decode("7e", 16))
	print(encode(45, 16))








