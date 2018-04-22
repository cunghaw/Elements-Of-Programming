# -*- coding: utf-8 -*-
"""
Compute a Gray code.
@author: Ronny
"""

def isBitDiffOne( num1, num2 ):
	xor = num1 ^ num2
	numBitDiff = 0
	while xor and numBitDiff < 2:
		if xor & 1:
			numBitDiff += 1
		xor = xor >> 1
	return numBitDiff == 1

def computeGrayCode( n ):
	numSet = set( [ x for x in range( 2 ** n ) ] )
	for num in numSet:
		res = [ num ]
		if computeGrayCodeHelper( res, numSet - set([ num ]) ):
			return res
		
	return []
	
def computeGrayCodeHelper( curr_num_list, numSet ):
	if not numSet:
		if isBitDiffOne( curr_num_list[0], curr_num_list[-1] ):
			return True
	else:
		for num in numSet:
			if isBitDiffOne( curr_num_list[-1], num ):
				curr_num_list.append( num )
				if computeGrayCodeHelper( curr_num_list, numSet - set( [ num ] ) ):
					return True
				else:
					curr_num_list.pop()
	return False
			
	
if __name__ == '__main__':
	assert( isBitDiffOne( 0, 1 ) == True )
	assert( isBitDiffOne( 1, 3 ) == True )
	assert( isBitDiffOne( 3, 2 ) == True )
	assert( isBitDiffOne( 0, 3 ) == False )	
	assert ( computeGrayCode( 3 ) == [0, 1, 3, 2, 6, 7, 5, 4] )
	
	print "All unit tests are passed"