# -*- coding: utf-8 -*-
"""
The interval covering problem
@author: Ronny
"""

def getMergedInterval( first, second ):
	if first[0] >= second[0] and first[0] <= second[0]:
		start = first[0]
	else:
		start = second[0]
	
	if first[1] >= second[0] and first[1] <= second[0]:
		end = first[1]
	else:
		end = second[1]
	return ( start, end )

def findMinInterval( intervals ):
	first = interval[0]
	for interval in intervals[1:]:
		first = getMergedInterval( first, interval )
	return first

if __name__ == '__main__':	
	intervals = [ (0,3), (2,6), (3,4), (6,9) ]
	assert( findMinInterval(intervals) == (3,6) )

	intervals = [ (1,2), (2,3), (3,4), (2,3), (3,4), (4,5) ]
	assert( findMinInterval(intervals) == (2,4) )

	print "All unit tests are passed"