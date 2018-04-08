# -*- coding: utf-8 -*-
"""
Compute the spiral ordering of a 2D array.
@author: Ronny
"""

def getSpiralPath( arr2d ):
	dim = len( arr2d ) - 1
	p = 0
	path = []
	for iter in range( 0, ( len( arr2d ) + 1 ) / 2 ):
		layer = dim / ( 2 ** iter )
		cx, cy = p, p	
		dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		for dir in dirs:
			for x in range( 0, layer ):
				if (cx >= p) and (cx <= dim - p) and (cy >= p) and (cy <= dim - p):
					path.append( arr2d[cy][cx] )
				cy += dir[0]
				cx += dir[1]
		p += 1
	return path
	
if __name__ == '__main__':
	arr2d = [ [ 1, 2, 3 ],
			  [ 4, 5, 6 ],
			  [ 7, 8, 9 ] ]
	assert( getSpiralPath( arr2d ) == [ 1, 2, 3, 6, 9, 8, 7, 4, 5 ] )

	arr2d = [ [ 1,   2,  3,  4 ],
			  [ 5,   6,  7,  8 ],
			  [ 9,  10, 11, 12 ],
			  [ 13, 14, 15, 16 ] ]
	assert( getSpiralPath( arr2d ) == [ 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10 ] )
	print "All unit tests are passed"