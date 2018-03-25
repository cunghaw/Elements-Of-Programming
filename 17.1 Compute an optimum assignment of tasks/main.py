# -*- coding: utf-8 -*-
"""
Compute an optimum assignment of tasks
@author: Ronny
"""

def computeOptimumTasks( tasks ):
	result = []
	len_half_tasks = len( tasks ) / 2
	tasks = sorted( tasks )
	for max_task, min_task in zip( reversed( tasks[ len_half_tasks: ] ), tasks[ :len_half_tasks ] ):
		result.append( ( min_task, max_task ) )
	return result
	
if __name__ == '__main__':	
	assert( computeOptimumTasks( [ 5, 2, 1, 6, 4, 4 ] ) == [ ( 1, 6 ), ( 2, 5 ), ( 4, 4 ) ] )

	print "All unit tests are passed"