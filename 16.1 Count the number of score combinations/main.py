# -*- coding: utf-8 -*-
"""
Count the number of score combinations.
@author: Ronny
"""

def countScoreCombination( totalScore, play_points ):
	collected_points_so_far = []
	latest_collected_points = set( [] )
	countScoreCombinationHelper( totalScore, play_points, collected_points_so_far, latest_collected_points )
	return len( latest_collected_points )

def countScoreCombinationHelper( totalScore, play_points, collected_points_so_far, latest_collected_points ):
	if totalScore - sum( collected_points_so_far ) < 0:
		pass
	elif totalScore == sum( collected_points_so_far ):
		latest_collected_points.add( tuple( sorted( collected_points_so_far ) ) )	
	else:
		for score in play_points:
			collected_points_so_far.append( score )
			countScoreCombinationHelper( totalScore, play_points, collected_points_so_far, latest_collected_points )
			collected_points_so_far.pop()
		
if __name__ == '__main__':	
	assert( countScoreCombination( 12, [ 2, 3, 7 ] ) == 4 )
	
	print "All unit tests are passed"