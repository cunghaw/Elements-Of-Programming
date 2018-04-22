# -*- coding: utf-8 -*-
"""
Compute Enclosed Regions
@author: Ronny
"""
	
B = True
W = False	
	
def isEnclosed( mat, cell_loc, len_y, len_x, cache_enclosed ):
	visited = set([])
	return isEnclosedHelper( mat, cell_loc, len_y, len_x, visited, cache_enclosed )
	
def isEnclosedHelper( mat, cell_loc, len_y, len_x, visited, cache_enclosed ):
	if cell_loc[0] < 0 or cell_loc[0] > len_y - 1 or cell_loc[1] < 0 or cell_loc[1] > len_x -1:
		return False
	elif mat[cell_loc[0]][cell_loc[1]] == B or cell_loc in visited:
		return True
	else:
		visited.add( cell_loc )
		dirs = [ ( 1, 0 ), ( -1, 0 ), ( 0, 1 ), ( 0, -1 ) ]
		res = True
		for dir in dirs:
			res &= isEnclosedHelper( mat, ( cell_loc[0] + dir[0], cell_loc[1] + dir[1] ), len_y, len_x, visited, cache_enclosed )
		
		if res:
			cache_enclosed.add( cell_loc )
		return res

def computeEncloseRegions( mat ):
	len_x = len( mat[0] )
	len_y = len( mat )
	cache_enclosed = set([])
	
	# iterate non-boundary cells
	for y in range( len_y -1 ):
		for x in range( len_x -1 ):
			if mat[y][x] != B:
				curr_cell_loc = ( y, x )
				if curr_cell_loc in cache_enclosed or isEnclosed( mat, curr_cell_loc, len_y, len_x, cache_enclosed ):
					mat[y][x] = B
	
if __name__ == '__main__':
	mat1 =   [[B, B, B, B],
			  [W, B, W, B],
			  [B, W, W, B],
			  [B, B, B, B]]
	
	cell_loc = ( 2, 1 )
	computeEncloseRegions( mat1 )
	assert( mat1 == [[B, B, B, B],
				     [W, B, B, B],
				     [B, B, B, B],
				     [B, B, B, B]])				 
	
	print "All unit tests are passed"