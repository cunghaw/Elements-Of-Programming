# -*- coding: utf-8 -*-
"""
Computing an alternation.
@author: Ronny
"""

def swap( array, idx1, idx2 ):
	temp = array[idx2]
	array[idx2] = array[idx1]
	array[idx1] = temp

def computeAlternation( array ):
	firstNumIdx = 0
	secondNumIdx = 1
	len_array = len( array )
	while secondNumIdx < len_array:
		# even number
		if ( firstNumIdx % 2 ) == 0:
			if array[firstNumIdx] > array[secondNumIdx]:
				swap( array, firstNumIdx, secondNumIdx )
		# odd number
		else:
			if array[firstNumIdx] < array[secondNumIdx]:
				swap( array, firstNumIdx, secondNumIdx )
		firstNumIdx += 1
		secondNumIdx += 1
	return array
	
if __name__ == '__main__':
	assert( computeAlternation( [ 1, 2, 3 ] ) == [ 1, 3, 2 ] )
	assert( computeAlternation( [ 1, 2, 3, 4, 5 ] ) == [ 1, 3, 2, 5, 4 ] )
	print "All unit tests are passed"