# -*- coding: utf-8 -*-
"""
Compute the right sibling tree.
@author: Ronny
"""

from collections import deque


# O(n) space solution
def setRightSibling( nextLevel ):
	head_index = 0
	max_index = len( nextLevel ) - 1
	while head_index < max_index:
		nextLevel[head_index].right_sibling = nextLevel[head_index + 1]
		head_index += 1
	
def computeRightSibling( root ):
	currentLevel = deque( [ root ] )
	nextLevel = deque( [] )
	while currentLevel:
		node = currentLevel.popleft()
		if node.left:
			nextLevel.append( node.left )
		if node.right:
			nextLevel.append( node.right )
		if len( currentLevel ) == 0:
			setRightSibling( nextLevel )
			currentLevel = nextLevel
			nextLevel = deque( [] )
	
def getLevelOrder( root, level ):
	return getLevelOrderHelper( root, level, 0 )
	
def getLevelOrderHelper( root, level, cLevel ):
	if level == cLevel:
		res = []
		while root:
			res.append( root.data )
			root = root.right_sibling
		return res
	elif cLevel > level:
		return []
	else:
		return getLevelOrderHelper( root.left, level, cLevel + 1 )
				
# O(1) space solution
def constructRightSibling( root ):
	if root:
		constructRightSiblingLowerNode( root )
		constructRightSibling( root.left )

def constructRightSiblingLowerNode( root ):
	while root:
		if root.left:
			root.left.right_sibling = root.right
		if root.right_sibling and root.right:
			root.right.right_sibling = root.right_sibling.left
		root = root.right_sibling

class BTNode:
	def __init__( self, **kwargs ):
		self.data = kwargs['data']
		self.left = kwargs['left']
		self.right = kwargs['right']
		self.right_sibling = None
			
if __name__ == '__main__':
	P = BTNode( data = 'P', left = None, right = None )
	Z = BTNode( data = 'Z', left = None, right = None )
	K = BTNode( data = 'K', left = None, right = None )
	U = BTNode( data = 'U', left = None, right = None )
	G = BTNode( data = 'G', left = None, right = None )
	L = BTNode( data = 'L', left = None, right = None )
	E = BTNode( data = 'E', left = None, right = None )
	D = BTNode( data = 'D', left = None, right = None )	
	O = BTNode( data = 'O', left = Z,    right = P )	
	J = BTNode( data = 'J', left = U,    right = K )	
	F = BTNode( data = 'F', left = L,    right = G )
	C = BTNode( data = 'C', left = D,    right = E )
	B = BTNode( data = 'B', left = C,    right = F )	
	I = BTNode( data = 'I', left = J,    right = O )	
	A = BTNode( data = 'A', left = B,    right = I )
	
	#computeRightSibling( A )
	constructRightSibling( A )
	assert( getLevelOrder( A, 0 ) == [ 'A' ] )
	assert( getLevelOrder( A, 1 ) == [ 'B', 'I' ] )
	assert( getLevelOrder( A, 2 ) == [ 'C', 'F', 'J', 'O' ] )
	assert( getLevelOrder( A, 3 ) == [ 'D', 'E', 'L', 'G', 'U', 'K', 'Z', 'P' ] )
	assert( getLevelOrder( A, 4 ) == [] )
	
	print "All unit tests are passed"