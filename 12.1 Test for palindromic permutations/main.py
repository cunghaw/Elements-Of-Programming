# -*- coding: utf-8 -*-
"""
Test for palindromic permutations.
@author: Ronny
"""
from collections import Counter 


def isPalindromic( word ):
	temp = Counter( word )
	for k, v in temp.items():
		temp[k] = v % 2
	return sum( temp.values() ) < 2
	

if __name__ == '__main__':
	assert( isPalindromic( "edified" ) == True )		
	assert( isPalindromic( "level" ) == True )
	assert( isPalindromic( "rotator" ) == True )
	assert( isPalindromic( "foobaraboof" ) == True )
	assert( isPalindromic( "roti" ) == False )
	
	print "All unit tests are passed"