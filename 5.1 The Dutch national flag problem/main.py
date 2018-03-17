# -*- coding: utf-8 -*-
"""
Quick sort implementation
@author: Ronny
"""

def quickSort ( array, low, high ):
	if ( low < high ):
		pi = partition ( array, low, high )
		quickSort ( array, low, pi - 1 )
		quickSort ( array, pi + 1, high )
	return array

def swap ( array, idx1, idx2 ):
	temp = array [ idx2 ]
	array [ idx2 ] = array [ idx1 ]
	array [ idx1 ] = temp

def partition ( array, low, high ):
	# Use last element for pivot
	pivot = array [ high ]
	i = low - 1
	while ( low < high ):
		if array [ low ] < pivot:
			i += 1
			swap ( array, i, low )
		low += 1
	i += 1
	swap ( array, i, high )
	return i

if __name__ == '__main__':
	# Test partition
	assert( partition( [ 1, 2, 3, 4, 5 ], 0, 4 ) == 4 )
	assert( partition( [ 5, 4, 3, 2, 1 ], 0, 4 ) == 0 )
	assert( partition( [ 5, 1, 4, 2, 3 ], 0, 4 ) == 2 )
	assert( partition( [ 1, 1, 4, 2, 3 ], 0, 4 ) == 3 )	
	
	# Test quickSort
	assert( quickSort( [ 1, 2, 3, 4, 5 ], 0, 4 ) == [ 1, 2, 3, 4, 5 ] )
	assert( quickSort( [ 5, 4, 3, 2, 1 ], 0, 4 ) == [ 1, 2, 3, 4, 5 ] )
	assert( quickSort( [ 5, 1, 4, 2, 3 ], 0, 4 ) == [ 1, 2, 3, 4, 5 ] )	
	assert( quickSort( [ 1, 1, 4, 2, 3 ], 0, 4 ) == [ 1, 1, 2, 3, 4 ] )	
	assert( quickSort( [ 3, 1, 3, 1, 3 ], 0, 4 ) == [ 1, 1, 3, 3, 3 ] )		
	assert( quickSort( [ 4, 3, 2, 1    ], 0, 3 ) == [ 1, 2, 3, 4    ] )		
	
	print "All unit tests are passed"