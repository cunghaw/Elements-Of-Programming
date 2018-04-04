# -*- coding: utf-8 -*-
"""
Compute the spreadsheet column encoding.
@author: Ronny
"""

# XX => X.26^1 + X.26^0
def computeColumnEncoding( col ):
	res = 0
	for idx, ch in enumerate( reversed( col ), 0 ):
		res += ( ord( ch ) - ord( 'A' ) + 1 ) * 26 ** idx
	return res
	
if __name__ == '__main__':
	assert( computeColumnEncoding( "A" ) == 1 )
	assert( computeColumnEncoding( "Z" ) == 26 )
	assert( computeColumnEncoding( "ZZ" ) == 702 )
	print "All unit tests are passed"