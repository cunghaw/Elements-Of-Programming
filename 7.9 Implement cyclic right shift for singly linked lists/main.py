# -*- coding: utf-8 -*-
"""
Implement cyclic right shift for singly linked lists.
@author: Ronny
"""
from __future__ import print_function

class Node:
	data = None
	next = None
	def __init__( self, **kwargs ):
		self.data = kwargs['data']
		self.next = kwargs['next']

def printLinkedList( head ):
	current = head
	while( current ):
		print( ' {0} '.format( current.data ), end = '' )
		current = current.next
	print( '' )

def performCyclicRightShift( head, k ):
	secondPtr = head
	lastSecondPtr = None
	while( secondPtr and k > 1 ):
		lastSecondPtr = secondPtr
		secondPtr = secondPtr.next
		k -= 1
	
	if k > 1:
		raise Exception( 'Invalid linked lists' )
	
	# find the tail node
	tailPtr = secondPtr
	while( tailPtr.next ):
		tailPtr = tailPtr.next
		
	tailPtr.next = head
	lastSecondPtr.next = None
	return secondPtr
	
			
if __name__ == '__main__':
	nd5 = Node( data = 2, next = None )
	nd4 = Node( data = 3, next = nd5  )
	nd3 = Node( data = 5, next = nd4 )
	nd2 = Node( data = 3, next = nd3 )
	nd1 = Node( data = 2, next = nd2 )
	printLinkedList( nd1 )
	newNd = performCyclicRightShift( nd1, 3 )
	printLinkedList( newNd )	
	
	print ( "All unit tests are passed" )