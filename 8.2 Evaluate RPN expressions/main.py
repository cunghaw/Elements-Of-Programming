# -*- coding: utf-8 -*-
"""
Evaluate RPN Expression.
@author: Ronny
"""

def evaluate( expression ):
	result = []
	exps = expression.split( ',' )
	for exp in exps:
		if not exp.isdigit() and len( exp ) == 1:
			num1 = result.pop()
			num2 = result.pop()
			if exp == '+':
				result.append( num1 + num2 )
			elif exp == '-':
				result.append( num1 - num2 )
			elif exp == 'x':
				result.append( num1 * num2 )
			elif exp == '/':
				result.append( num2 / num1 )
			else:
				raise Exception( 'Unknown operator : {}'.format( exp ) )
		else:
			result.append( int( exp ) )
	return result.pop()
			
if __name__ == '__main__':
	assert( evaluate( "3,4,+,2,x,1,+" ) == 15 )
	assert( evaluate( "1729" ) == 1729 )
	assert( evaluate( "1,1,+,-2,x" ) == -4 )
	assert( evaluate( "-641,6,/,28,/" ) == -4 )	
	print "All unit tests are passed"