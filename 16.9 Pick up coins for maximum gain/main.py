# -*- coding: utf-8 -*-
"""
Pick up coins for maximum gain
@author: Ronny
"""

def pickMaximumGain( coins ):
	return pickMaximumGainHelper( coins, 0, len( coins ) - 1 )
	
def pickMaximumGainHelper( coins, a, b ):
	if not a <= b:
		return 0
	else:
		pick_a = coins[a] + min( pickMaximumGainHelper( coins, a + 2, b ), pickMaximumGainHelper( coins, a + 1, b - 1 ) )
		pick_b = coins[b] + min( pickMaximumGainHelper( coins, a + 1, b - 1 ), pickMaximumGainHelper( coins, a, b - 2 ) )
		return max( pick_a, pick_b )

	
if __name__ == '__main__':	
	assert( pickMaximumGain( [ 10, 25, 5, 1, 10, 5 ] ) == 31 )
	assert( pickMaximumGain( [ 25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10 ] ) == 140 )
	
	print "All unit tests are passed"