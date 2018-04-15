# -*- coding: utf-8 -*-
"""
Implement a circular queue.
@author: Ronny
"""

class CircularQueue:
	def __init__( self, size ):
		self.array = [ None ] * size
		self.max_size = size
		self.begin = 0
		self.end = 0
		self.num_elements = 0

	def size( self ):
		return self.num_elements
	
	def enqueue( self, data ):
		if self.num_elements == self.max_size:
			max_size = 2 * self.max_size
			temp = [ None ] * ( max_size )
			begin = 0
			while self.size():
				temp[begin] = self.dequeue()
				begin += 1
			self.array = temp
			self.begin = 0
			self.end = begin
			self.num_elements = self.max_size			
			self.max_size = max_size
	
		self.array[self.end] = data
		self.num_elements += 1
		self.end += 1
		self.end = self.end % self.max_size
			
	def dequeue( self ):
		if self.num_elements == 0:
			raise Exception()
		
		res = self.array[self.begin]	
		self.num_elements -= 1	
		self.array[self.begin] = None
		self.begin += 1
		self.begin = self.begin % self.max_size
		return res
			
if __name__ == '__main__':
	
	queue = CircularQueue( 5 )
	
	queue.enqueue( 1 )
	assert( queue.size() == 1 )
	queue.enqueue( 2 )
	assert( queue.size() == 2 )	
	queue.enqueue( 3 )		
	assert( queue.size() == 3 )
	
	assert( queue.dequeue() == 1 )
	assert( queue.size() == 2 )
	assert( queue.dequeue() == 2 )
	assert( queue.size() == 1 )
	
	queue.enqueue( 1 )
	queue.enqueue( 2 )
	queue.enqueue( 3 )
	queue.enqueue( 4 )
	queue.enqueue( 5 ) 
	
	assert( queue.size() == 6 )
	assert( queue.dequeue() == 3 )
	assert( queue.dequeue() == 1 )
	assert( queue.dequeue() == 2 )
	assert( queue.dequeue() == 3 )
	assert( queue.dequeue() == 4 )
	assert( queue.dequeue() == 5 )					
	
	print "All unit tests are passed"