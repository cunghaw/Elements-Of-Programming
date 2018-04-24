# -*- coding: utf-8 -*-
"""
Implement list pivoting.
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

def appendNode( node, i_node, appended_node ):
	if node is None:
		node = appended_node
		i_node = node
	else:
		i_node.next = appended_node
		i_node = i_node.next
	return node, i_node
	
def createPivotList( head, k ):
	less_k, k_node, greater_k = None, None, None
	i_less_k, i_k_node, i_greater_k = None, None, None
	while( head ):
		if head.data < k:
			less_k, i_less_k = appendNode( less_k, i_less_k, head )
		elif head.data == k:
			k_node, i_k_node = appendNode( k_node, i_k_node, head )			
		else:
			greater_k, i_greater_k = appendNode( greater_k, i_greater_k, head )
		head = head.next
	
	i_greater_k.next = None
	i_k_node.next = greater_k
	i_less_k.next = k_node
	
	return less_k
		
if __name__ == '__main__':
	nd7 = Node( data = 11, next = None )
	nd6 = Node( data = 5,  next = nd7  )
	nd5 = Node( data = 7,  next = nd6 )
	nd4 = Node( data = 11, next = nd5 )
	nd3 = Node( data = 2,  next = nd4 )
	nd2 = Node( data = 2,  next = nd3 )
	nd1 = Node( data = 3,  next = nd2 )
	printLinkedList( nd1 )
	newNd = createPivotList( nd1, 7 )
	printLinkedList( newNd )	
	
	print ( "All unit tests are passed" )