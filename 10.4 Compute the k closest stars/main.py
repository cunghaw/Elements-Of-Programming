# -*- coding: utf-8 -*-
"""
Compute the k closest stars.
@author: Ronny
"""

import heapq
import math

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
	
class MaxHeap( Heap ):

	def heappush( self, x ): 
		heapq.heappush( self.data, MaxHeapify( x ) )

	def heappop( self ): 
		return heapq.heappop( self.data ).num
	
	def top( self ):
		return self.data[0].num	
	
class Point( object ):
	def __init__( self, **kwargs ):
		self.x = kwargs[ 'x' ]
		self.y = kwargs[ 'y' ]
		self.z = kwargs[ 'z' ]
		
	def __lt__( self, other ):
		distance = math.sqrt( self.x ** 2 + self.y ** 2 + self.z ** 2 )
		o_distance = math.sqrt( other.x ** 2 + other.y ** 2 + other.z ** 2 )
		return distance < o_distance
		
	def __eq__( self, other ):
		distance = math.sqrt( self.x ** 2 + self.y ** 2 + self.z ** 2 )
		o_distance = math.sqrt( other.x ** 2 + other.y ** 2 + other.z ** 2 )
		return distance == o_distance
	
	def __str__( self ):
		return " {0} {1} {2} ".format( self.x, self.y, self.z )

def getKClosestCoordinate( coordinates, k ):
	mHeap = MaxHeap()
	for point in coordinates:
		if len( mHeap ) < k:
			mHeap.heappush( point )
		else:
			if mHeap.top() > point:
				mHeap.heappop()
				mHeap.heappush( point )
				
	res = []
	while len( mHeap ) > 0:
		res.append( mHeap.heappop() )
	return res
			
if __name__ == '__main__':
	A, B, C, D, E, F = Point( x = 1, y = 0, z = 0 ), Point( x = 1, y = 1, z = 0 ), Point( x = 1, y = 1, z = 1 ), Point( x = 2, y = 2, z = 2 ), Point( x = 2, y = -1, z = 3 ), Point( x = 0, y = 1, z = 0 )
	coordinates = [ A, B, C, D, E, F ]
	
	assert( A < B )
	assert( C > B )
	assert( A == F )
	
	assert( getKClosestCoordinate( coordinates, 1 ) == [ A ] ) 
	assert( getKClosestCoordinate( coordinates, 2 ) == [ F, A ] ) 
	assert( getKClosestCoordinate( coordinates, 3 ) == [ B, F, A ] ) 
	
	print "All unit tests are passed"