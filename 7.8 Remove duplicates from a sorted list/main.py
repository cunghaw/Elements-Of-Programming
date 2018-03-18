# -*- coding: utf-8 -*-
"""
Remove duplicates from a sorted list.
@author: Ronny
"""

def removeDuplicates( sortedList ):
	last_data = None
	idx = 0
	for curr_data in sortedList[:]:
		if last_data == curr_data:
			del sortedList[idx]
		else:
			last_data = curr_data
			idx += 1

	return sortedList
			
if __name__ == '__main__':
	assert( removeDuplicates( [ 1, 2, 2, 3 ] ) == [ 1, 2, 3 ] )
	assert( removeDuplicates( [ 1, 2, 3 ] ) == [ 1, 2, 3 ] )
	assert( removeDuplicates( [ 1, 1, 1 ] ) == [ 1 ] )
	print "All unit tests are passed"