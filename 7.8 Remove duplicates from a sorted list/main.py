# -*- coding: utf-8 -*-
"""
Base convertion.
@author: Ronny
"""

TABLE_STR_NUM = { '0' : 0,  '1' : 1,  '2' : 2,  '3' : 3, 
                  '4' : 4,  '5' : 5,  '6' : 6,  '7' : 7, 
				  '8' : 8,  '9' : 9,  'A' : 10, 'B' : 11,
				  'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15  }

TABLE_NUM_STR = { k : v for v, k in TABLE_STR_NUM.items() }

def convert ( strNum, base1, base2 ):
	total = 0
	for mul, char in enumerate( reversed( strNum ), 0 ):
		total += ( base1 ** mul ) * TABLE_STR_NUM[char]
	
	result = ""
	while ( total > 0 ):
		num = int( total / base2 )
		mod = total % base2
		result = "%s%s" % ( TABLE_NUM_STR[ mod ], result ) 
		total = num
	return result
	
if __name__ == '__main__':
	assert( convert( "615", 7, 13 ) == "1A7" )
	assert( convert( "1A7", 13, 7 ) == "615" )
	assert( convert( "615", 7, 2  ) == '100110010' )
	assert( convert( "1A7", 13, 2 ) == '100110010' )
	print "All unit tests are passed"