# -*- coding: utf-8 -*-
"""
Test a string over for well-formedness.
@author: Ronny
"""

def isMatch( exp1, exp2 ):
	if ( exp1 == '(' and exp2 == ')' ) or \
	   ( exp1 == '[' and exp2 == ']' ) or \
	   ( exp1 == '{' and exp2 == '}' ):
	    return True
	else:
		return False

def checkFormedness( expression ):
	temp = []
	for exp in reversed( expression ):
		if temp:
			if isMatch( exp, temp[-1] ):
				temp.pop()
				continue
		temp.append( exp )
	return not temp
			
if __name__ == '__main__':
	assert( checkFormedness( "([]){()}" ) == True )
	assert( checkFormedness( "[()[]{()()}]" ) == True )
	assert( checkFormedness( "{)" ) == False )
	assert( checkFormedness( "[()[]{()()" ) == False )
	
	print "All unit tests are passed"