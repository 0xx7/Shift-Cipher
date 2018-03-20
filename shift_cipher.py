'''
#Author: Abdul Azeez Omar
#Date: Feb 2017
#Purpose: An implementation of a basic shift cipher (Caesar Cipher) in python.
'''

import sys

if __name__ == '__main__':

	print('what do u want to do?')
	print('1: encode')
	print('2: decode')

	choice = input('please enter your choice: ')
	if choice != '1' and choice != '2':
		print('Invalid choice')
		sys.exit(1)

	input_str = input('Please enter the input message: ')
	input_str = input_str.lower()

	if choice == '1':
		shift = 3
		results = []
		for c in input_str:
			if ord(c) >= ord('a') and ord(c) <= ord('z'):
				results.append(chr(ord('a') + (ord(c) - ord('a') + shift) % 26))
			else:
				results.append(c)

		result_str = ''.join(results)
		print('The encoded message with key number %d is: %s' % (shift, result_str))
	else:
		for shift in range(26):
			results = []
			for c in input_str:
				if ord(c) >= ord('a') and ord(c) <= ord('z'):
					results.append(chr(ord('a') + (ord(c) - ord('a') - shift + 26) % 26))
				else:
					results.append(c)

			result_str = ''.join(results)
			print('The decoded message with key number %2d is: %s' % (shift, result_str))