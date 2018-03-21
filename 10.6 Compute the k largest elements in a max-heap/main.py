# -*- coding: utf-8 -*-
"""
Compute the k largest elements in a max-heap.
@author: Ronny
"""

import operator

def getLargestElements( heap, k ):
	curr_nodes = { 0 : heap[ 0 ] }
	result = []
	len_heap = len( heap )
	
	while len( result ) < k and len( curr_nodes ) > 0:
		max_node = max( curr_nodes.iteritems(), key = operator.itemgetter( 1 ) )
		result.append( max_node[ 1 ] )
		curr_nodes.pop( max_node[ 0 ] )
		left_child_idx = 2 * max_node[ 0 ] + 1
		right_child_idx = 2 * max_node[ 0 ] + 2
		if left_child_idx < len_heap:
			curr_nodes[ left_child_idx ] = heap[ left_child_idx ]
		if right_child_idx < len_heap:
			curr_nodes[ right_child_idx ] = heap[ right_child_idx ]
				
	return result
			
if __name__ == '__main__':
	heap = [ 561, 314, 401, 28, 156, 359, 271, 11, 3 ]
	assert( set( getLargestElements( heap, 1 ) ) == set( [ 561 ] ) )
	assert( set( getLargestElements( heap, 2 ) ) == set( [ 561, 401 ] ) )	
	assert( set( getLargestElements( heap, 3 ) ) == set( [ 561, 401, 359 ] ) )
	assert( set( getLargestElements( heap, 4 ) ) == set( [ 561, 401, 359, 314 ] ) )
	assert( set( getLargestElements( heap, 5 ) ) == set( [ 561, 401, 359, 314, 271 ] ) )	
	print "All unit tests are passed"