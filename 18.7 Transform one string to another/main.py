# -*- coding: utf-8 -*-
"""
Transform one string to another.
@author: Ronny
"""

def calcDistance( str1, str2 ):
	diff = 0
	for ch1, ch2 in zip( str1, str2 ):
		if ch1 != ch2:
			diff += 1
	return diff

def getClosestNeighbors( str1, setWords ):
	result = set([])
	for word in setWords:
		if calcDistance( str1, word ) == 1:
			result.add( word )
	return result

def transform( start, end, setWords ):
	if start == end:
		return [start]
	else:		
		if not setWords:
			return []
		else:
			neighbors = getClosestNeighbors( start, setWords )
			if neighbors:
				result = [start]
				temp = {}
				for neighbor in neighbors:
					paths = transform( neighbor, end, setWords - neighbors - set(result) )
					if len( paths ) > 0:
						temp[neighbor] = paths
				
				if temp:
					min_node_len = min( [ len(v) for v in temp.values() ] )
					for k,v in temp.items():
						if len(v) == min_node_len:
							result = result + v
							return result
				return []					
			else:
				return []
	

if __name__ == '__main__':
	assert( calcDistance( 'cat', 'cat') == 0 )
	assert( calcDistance( 'cat', 'cot') == 1 )
	assert( calcDistance( 'gat', 'cot') == 2 )

	setWords = set( ['bat', 'cot', 'dog', 'dag', 'dot', 'cat'] )	
	assert( getClosestNeighbors( 'cat', setWords ) == set([ 'bat', 'cot']) )
	assert( getClosestNeighbors( 'dog', setWords ) == set([ 'dag', 'dot']) )	

	assert( transform( 'cat', 'dog', setWords ) == ['cat', 'cot', 'dot', 'dog'] )

	setWords = set( ['bat', 'cot', 'dit', 'dut', 'deg' ,'dog', 'dag', 'dot', 'cat'] )
	assert( transform( 'cat', 'dog', setWords ) == ['cat', 'cot', 'dot', 'dog'] )
	assert( transform( 'cat', 'dos', setWords ) == [] )	
	
	setWords = set( ['cat', 'bat', 'pat', 'pot', 'cot'] )
	assert( transform( 'cat', 'cot', setWords ) == ['cat', 'cot'] )
	
	print "All unit tests are passed"