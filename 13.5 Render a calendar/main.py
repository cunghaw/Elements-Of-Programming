# -*- coding: utf-8 -*-
"""
Render a calendar
@author: Ronny
"""

def getConcurrentMaximumEvents( events ):
	start = []
	stop = []
	max_event_so_far = 0
	curr_max_event = 0
	
	for evt in events:
		start.append( evt[0] )
		stop.append( evt[1] )

	start = sorted( start )
	stop = sorted( stop )
	
	i = 0
	j = 0
	len_events = len( events )
	while ( i < len_events and j < len_events ):
		if start[i] < stop[j]:
			i += 1
			curr_max_event +=1
			if max_event_so_far < curr_max_event:
				max_event_so_far = curr_max_event
		elif start[i] == stop[j]:
			i += 1
			j += 1
		else:
			j +=1
			curr_max_event -= 1

	return max_event_so_far
	
	
if __name__ == '__main__':
	events1 = [ ( 1, 5 ), ( 6, 10 ), ( 11, 13 ), ( 14, 15 ), ( 2, 7 ),
			   ( 8, 9 ), ( 12, 15 ), (  4, 5  ), ( 9, 17 ) ]
	events2 = [ ( 1, 2 ), ( 1, 2 ), ( 1, 2 ), ( 3, 5 ), ( 1, 10 ) ]
	events3 = [ ( 1, 2 ), ( 3, 4 ), ( 5, 6 ), ( 7, 8 ), ( 9, 10 ) ]
	
	assert( getConcurrentMaximumEvents( events1 ) == 3 )
	assert( getConcurrentMaximumEvents( events2 ) == 4 )	
	assert( getConcurrentMaximumEvents( events3 ) == 1 )
	
	print "All unit tests are passed"