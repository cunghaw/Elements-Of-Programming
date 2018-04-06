# -*- coding: utf-8 -*-
"""
Count the number of moves to climb stairs.
@author: Ronny
"""

def countNumberOfWays( n, k ):
	cache = [0] * ( n + 1 )
	return countNumberOfWaysHelper( n, k, cache )
	
		
def countNumberOfWaysHelper( n, k, cache ):
	if cache[n] == 0:
		if n == 0:
			cache[n] = 1
		elif n == 1:
			cache[n] = 1
		elif n < k:
			return 0
		else:
			res = 0
			for x in range( 1, k + 1 ):
				res += countNumberOfWays( n -x, k )
			cache[n] = res

	return cache[n]
		
if __name__ == '__main__':	
	assert( countNumberOfWays( 4, 2 ) == 5 )
	
	print "All unit tests are passed"