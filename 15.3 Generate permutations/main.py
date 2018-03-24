# -*- coding: utf-8 -*-
"""
Generate permutations
@author: Ronny
"""

def generatePermutation( str ):
	result = []
	generatePermutationHelper( '', str, result )
	return result
	
def generatePermutationHelper( start, end, result ):
	if len( end ) == 1:
		result.append( start + end )
		print start + end
	else:
		for ch in end:
			generatePermutationHelper( start + ch, ''.join( end.split( ch ) ), result )
	
if __name__ == '__main__':	
	assert( len( generatePermutation( 'abc' ) ) == 6 )
	assert( len( generatePermutation( 'abcd' ) ) == 24 )
	
	print "All unit tests are passed"