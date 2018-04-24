# -*- coding: utf-8 -*-
"""
Compute all valid IP addresses.
@author: Ronny
"""

def checkRange( ip_str ):
	if len( ip_str ) > 3:
		return False
		
	if len( ip_str ) > 1 and ip_str[0] == '0':
		return False
		
	if int( ip_str ) <= 255 and int( ip_str ) >= 0:
		return True
	else:
		return False

def findAllValidIP( ip ):
	len_ip = len( ip )
	valid_IPs = []
	for idx in range( 1, len_ip ):
		if checkRange( ip[:idx] ):
			for idy in range( idx + 1, len_ip ):
				if checkRange( ip[idx:idy] ):
					for idz in range( idy + 1, len_ip ):
						if checkRange( ip[idy:idz] ) and checkRange( ip[idz:] ):
							valid_IPs.append( '{0}.{1}.{2}.{3}'.format( ip[:idx], ip[idx:idy], ip[idy:idz], ip[idz:] ) )

	print valid_IPs
	return len( valid_IPs )
		

if __name__ == '__main__':
	assert( findAllValidIP( "19216811" ) == 9 )
	assert( findAllValidIP( "19210011" ) == 5 )
	print "All unit tests are passed"