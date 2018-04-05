# -*- coding: utf-8 -*-
"""
Compute the median of online data.
@author: Ronny
"""

import heapq

class MaxHeapify( object ):
	def __init__( self, num ): 
		self.num = num
		
	def __lt__( self, other ): 
		return self.num > other.num

	def __eq__( self, other ): 
		return self.num == other.num


class Heap( object ):

	def __init__( self ):
		self.data = []

	def __len__( self ): 
		return len( self.data )

class MinHeap( Heap ):

	def heappush( self, x ): 
		heapq.heappush( self.data, x )
		
	def heappop( self ): 
		return heapq.heappop( self.data )
		
	def top( self ):
		return self.data[0]		
	
class MaxHeap( Heap ):

	def heappush( self, x ): 
		heapq.heappush( self.data, MaxHeapify( x ) )

	def heappop( self ): 
		return heapq.heappop( self.data ).num
	
	def top( self ):
		return self.data[0].num	
 
def calculateMedian( array ):
	res = []
	minHeap = MinHeap()
	maxHeap = MaxHeap()
	maxHeap.heappush( array[0] )
	res.append( array[0] )
	for num in array[1:]:
		if num < maxHeap.top():
			maxHeap.heappush( num )
		else:
			minHeap.heappush( num )
	
		if len( maxHeap ) - len( minHeap ) > 1:
			minHeap.heappush( maxHeap.heappop() )
		elif len( minHeap ) > len( maxHeap ):
			maxHeap.heappush( minHeap.heappop() )
			
		if len( maxHeap ) == len( minHeap ):
			res.append( float( maxHeap.top() + minHeap.top() ) / 2 )
		else:
			res.append( maxHeap.top() )
			
	return res
 
if __name__ == '__main__':
	array = [ 1, 0, 3, 5, 2, 0, 1 ]
	assert( calculateMedian( array ) == [ 1, 0.5, 1, 2, 2, 1.5, 1 ] )
	
	print "All unit tests are passed"