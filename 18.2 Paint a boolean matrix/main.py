# -*- coding: utf-8 -*-
"""
Paint a boolean matrix
@author: Ronny
"""
	
def paintMatrix( arr2d, cell_loc, color ):
	curr_color = arr2d[cell_loc[0]][cell_loc[1]]
	dim = len( arr2d )
	visited = [ [False] * dim for x in range( dim ) ]
	paintMatrixHelper( arr2d, cell_loc, color, curr_color, dim - 1, visited )
	
def paintMatrixHelper( arr2d, cell_loc, set_color, read_color, max_idx, visited ):
	if cell_loc[0] < 0 or cell_loc[0] > max_idx or cell_loc[1] < 0 or cell_loc[1] > max_idx or arr2d[cell_loc[0]][cell_loc[1]] != read_color or visited[cell_loc[0]][cell_loc[1]] == True:
		return
	else:
		arr2d[cell_loc[0]][cell_loc[1]] = set_color
		visited[cell_loc[0]][cell_loc[1]] = True
		dirs = [ ( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 ) ]
		for dir in dirs:
			paintMatrixHelper( arr2d, ( cell_loc[0] + dir[0], cell_loc[1] + dir[1] ), set_color, read_color, max_idx, visited )
	
if __name__ == '__main__':
	mat =   [[True,  False, False],
			[True,  True,  True ],
			[False, False, False]]

	paintMatrix( mat, ( 0, 1 ), True )
	assert( mat == [[True,  True,  True],
					[True,  True,  True],
					[False, False, False]])

	paintMatrix( mat, ( 2, 0 ), False )
	assert( mat == [[True,  True,  True],
					[True,  True,  True],
					[False, False, False]])

	mat =   [[False, False, False],
			 [True,  False, True ],
			 [True,  False, True ]]

	paintMatrix( mat, ( 2, 2 ), False )
	assert( mat == [[False, False, False],
					[True,  False, False],
					[True,  False, False]])

	
	print "All unit tests are passed"