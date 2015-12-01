#Author: Vishwajith Upendra

import argparse

def string_rev(string):
	return string[::-1]

def main():
	parser = argparse.ArgumentParser(description='Reverse a given string')
	parser.add_argument('-s', action='store', dest='string', help='String to be reversed')
	results = parser.parse_args()
	'''Program to reverse an input string'''
	
	print "\nString to be reversed : ",results.string
	
	reversed_string=string_rev(results.string)
	
	print "\nReversed string : ",reversed_string
	
if __name__ == "__main__":
    main()
	