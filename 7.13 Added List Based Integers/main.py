# -*- coding: utf-8 -*-
"""
Added List Based Integers.
@author: Ronny
"""

from __future__ import print_function

class NodeList:
	def __init__( self, **kwargs ):
		self.data = kwargs[ 'data' ]
		self.next = kwargs[ 'next' ]

def createLinkedList( array ):
	head = NodeList( data = array[0], next = None )
	current = head
	for e in array[1:]:
		current.next = NodeList( data = e, next = None )
		current = current.next
	return head

def printLinkedList( head ):
	while head:
		print( '{0} '.format( head.data ), end = '' )
		head = head.next
	print( '' )

def add( num1, num2, carrier ):
	sum = num1 + num2 + carrier
	carrier = sum / 10
	sum = sum % 10
	current = NodeList( data = sum, next = None )
	return carrier, current
			
def addLinkedList( a, b ):
	carrier = 0
	head = None
	current = None
	res = []
	
	while a or b or carrier:
		carrier, node = add( a.data if a else 0, b.data if b else 0, carrier )
		res.append( node.data )
		if head is None:
			head = node
			current = node
		else:
			current.next = node
			current = current.next
		a = a.next if a else None
		b = b.next if b else None
		
	return head, res			
			
if __name__ == '__main__':
	headNode1 = createLinkedList( [3, 1, 4] )
	headNode2 = createLinkedList( [7, 0, 9] )
	
	head, res = addLinkedList( headNode1, headNode2 )
	printLinkedList( head )
	assert( res == [ 0, 2, 3, 1 ])
	
	head, res = addLinkedList( headNode1, None )
	printLinkedList( head )
	assert( res == [ 3, 1, 4 ])

	head, res = addLinkedList( None, headNode2 )
	printLinkedList( head )
	assert( res == [ 7, 0, 9 ])
	
	print ( "All unit tests are passed" )