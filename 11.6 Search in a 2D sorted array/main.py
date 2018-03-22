# -*- coding: utf-8 -*-
"""
Search in a 2D sorted array.
@author: Ronny
"""

def findNumber( array2d, number ):
	return findNumberHelper( array2d, number, 0, 0, len( array2d[0] ) -1, len( array2d ) -1 )
	
def findNumberHelper( array2d, number, x_start, y_start, x_end, y_end ):
	if number == array2d[y_start][x_start] or number == array2d[y_start][x_end] or number == array2d[y_end][x_start] or number == array2d[y_end][x_end]:
		return True
	else:	
		x_mid = x_start + ( x_end - x_start ) / 2
		y_mid = y_start + ( y_end - y_start ) / 2
		
		if number > array2d[y_start][x_start] and number <= array2d[y_mid][x_mid]:
			top_left = findNumberHelper( array2d, number, x_start, y_start, x_mid, y_mid )
		else:
			top_left = False
		
		if x_mid + 1 <= x_end and number >= array2d[y_start][x_mid + 1] and number <= array2d[y_mid][x_end]:
			top_right = findNumberHelper( array2d, number, x_mid, y_start, x_end, y_mid )
		else:
			top_right = False
		
		if y_mid + 1 <= y_end and number >= array2d[y_mid + 1][x_start] and number <= array2d[y_end][x_mid]:
			bottom_left = findNumberHelper( array2d, number, x_start, y_mid, x_mid, y_end )
		else:
			bottom_left = False
			
		if x_mid + 1 <= x_end and y_mid + 1 <= y_end and number >= array2d[y_mid + 1][x_mid + 1] and number < array2d[y_end][x_end]:
			bottom_right = findNumberHelper( array2d, number, x_mid, y_mid, x_end, y_end )
		else:
			bottom_right = False

		return top_left or top_right or bottom_left or bottom_right
			
if __name__ == '__main__':
	array2d = [ [ -1,  2,  4,  4,  6  ],
			    [  1,  5,  5,  9,  21 ], 
			    [  3,  6,  6,  9,  22 ],
			    [  3,  6,  8, 10,  24 ],
			    [  6,  8,  9, 12,  25 ],
			    [  8, 10, 12, 13,  40 ] ]

	assert( findNumber( array2d, 1  ) == True  )	
	assert( findNumber( array2d, 6  ) == True  )
	assert( findNumber( array2d, 40 ) == True  )
	assert( findNumber( array2d, 8  ) == True  )
	assert( findNumber( array2d, 9  ) == True  )
	assert( findNumber( array2d, 13 ) == True  )
	assert( findNumber( array2d, 12 ) == True  )
	assert( findNumber( array2d, 3  ) == True  )    
	assert( findNumber( array2d, -1 ) == True  )
	assert( findNumber( array2d, 7  ) == False )
	assert( findNumber( array2d, 15 ) == False )
	assert( findNumber( array2d, 11 ) == False )
	assert( findNumber( array2d, 17 ) == False )	
	
	print "All unit tests are passed"