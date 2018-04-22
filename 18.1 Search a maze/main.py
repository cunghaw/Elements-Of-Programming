# -*- coding: utf-8 -*-
"""
Search a maze
@author: Ronny
"""

import sys

def findPath( arr2d, start, end ):
	visited = [ [False] * len( arr2d ) for x in range( len( arr2d ) ) ]
	return findPathHelper( arr2d, start, end, visited )
		
def findPathHelper( arr2d, start, end, visited ):
	if start == end:
		return [end]
	elif ( start[0] < 0 ) or ( start[0] > len( arr2d ) - 1 ) or ( start[1] < 0 ) or ( start[1] > len( arr2d ) - 1 ) or \
		 ( arr2d[start[0]][start[1]] == 1 ) or ( visited[start[0]][start[1]] == True ):
		return []
	else:
		visited[start[0]][start[1]] = True
		resTop = findPathHelper( arr2d, ( start[0] -1, start[1] ), end, visited )
		resBot = findPathHelper( arr2d, ( start[0] +1, start[1] ), end, visited )
		resLeft = findPathHelper( arr2d, ( start[0], start[1] - 1 ), end, visited )
		resRight = findPathHelper( arr2d, ( start[0], start[1] + 1 ), end, visited )
		min_len = sys.maxint
		min_res = []
		for len_res, res in [ ( len( resTop ), resTop ), ( len( resBot ), resBot ), ( len( resLeft ), resLeft) , ( len( resRight ), resRight ) ]:
			if len_res != 0 and len_res < min_len:
				min_len, min_res = len_res, res
		if min_res:
			return [(start[0], start[1])] + min_res
		else:
			visited[start[0]][start[1]] = False
			return []
		
if __name__ == '__main__':
	maze = [[1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
			[0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
			[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
			[1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
			[0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]

	start = ( 9, 0 )
	end   = ( 0, 9 )
	print findPath( maze, start, end )

	print "All unit tests are passed"