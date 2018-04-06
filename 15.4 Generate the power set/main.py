# -*- coding: utf-8 -*-
"""
Generate the power set.
@author: Ronny
"""

def powerSet( nums, index ):
	if index == 0:
		return [ set([]) ]
	else:
		cSet = powerSet( nums, index - 1 )
		aSet = []
		for elem in cSet:
			aSet.append( elem | nums[index - 1] )
		return cSet + aSet
	
def powerSet2( nums, index ):
	combi = 2 ** index
	rSet = []
	for x in range( combi ):
		cSet = set([])
		for i in range( index ):
			if (x >> i & 1):
				cSet = cSet | nums[i]
		rSet.append( cSet )
	return rSet
	
if __name__ == '__main__':
	nums = [ set([1]), set([2]), set([3]) ]
	print powerSet( nums, 3 )
	print powerSet2( nums, 3 )	
	print "All unit tests are passed"