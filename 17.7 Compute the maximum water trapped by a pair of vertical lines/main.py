# -*- coding: utf-8 -*-
"""
Compute the maximum water trapped by a pair of vertical lines.
@author: Ronny
"""

def computeMaxWaterTrapped( array ):
	max_area_so_far = 0
	curr_area = 0
	left_idx = 0
	right_idx = len( array ) - 1
	
	while( left_idx < right_idx ):
		curr_area = ( right_idx - left_idx ) * min( array[left_idx], array[right_idx] )
		if curr_area > max_area_so_far:
			max_area_so_far = curr_area
		if array[right_idx] < array[left_idx]:
			right_idx -= 1
		else:
			left_idx += 1
		
	return max_area_so_far

if __name__ == '__main__':	
	array = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
	assert( computeMaxWaterTrapped( array ) == 48 )
	
	print "All unit tests are passed"