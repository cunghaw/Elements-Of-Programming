# -*- coding: utf-8 -*-
"""
Clone a graph
@author: Ronny
"""

class Node:
	data = None
	edges = None
	
	def __init__( self, data ):
		self.data = data
		self.edges = {}
		
	def addNeighbor( self, node ):
		if node.data not in self.edges:
			self.edges[ node.data ] = node
		else:
			raise Exception( 'Failed to add neighbor since it is already existed!' )

	def __str__( self ):
		return "data: " + str( self.data ) + " neighbor: " +  str( self.edges )

def clone( root ):
	visited = set()
	return cloneHelper( root, visited )

def cloneHelper( root, visited ):
	if root is None or root.data in visited:
		return
	
	visited.add( root.data )
	root_c = Node( root.data )
	for idx in root.edges:
		node_c = cloneHelper( root.edges[idx], visited )
		if node_c:
			root_c.addNeighbor( node_c )

	return root_c
	
if __name__ == '__main__':
	root = Node( 1 )
	root.addNeighbor( Node( 2 ) )
	root.addNeighbor( Node( 3 ) )
	assert( clone( root ) is not None )
	print str( root )
	print str( clone( root ) )

	print "All unit tests are passed"