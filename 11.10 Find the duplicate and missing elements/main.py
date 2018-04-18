# -*- coding: utf-8 -*-
"""
Find the duplicate and missing elements.
@author: Ronny
"""

	
def findDuplicateAndMissing( array ):
	arrXor, seqXor = 0, 0
	for idx, e in enumerate( array ):
		arrXor ^= e
		seqXor ^= idx

	diffBit = arrXor ^ seqXor
	theLeastSetBit = diffBit & ~( diffBit - 1 )
	
	dupXor, repXor = 0, 0
	for idx, e in enumerate( array ):
		if theLeastSetBit & idx > 0:
			dupXor ^= idx
		else:
			repXor ^= idx
		if theLeastSetBit & e > 0:
			dupXor ^= e
		else:
			repXor ^= e			
			
	if diffBit ^ dupXor == arrXor:
		return dupXor, repXor
	else:
		return repXor, dupXor
			
if __name__ == '__main__':
	assert( findDuplicateAndMissing( [0, 1, 2, 4, 4] ) == (4,3) )
	assert( findDuplicateAndMissing( [0, 1, 2, 3, 4, 5, 6, 7, 8, 8] ) == (8,9) )	
	assert( findDuplicateAndMissing( [0, 1, 1, 3, 4, 5, 6, 7, 8, 9] ) == (1,2) )	
	print "All unit tests are passed"