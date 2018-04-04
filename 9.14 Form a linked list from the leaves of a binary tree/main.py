# -*- coding: utf-8 -*-
"""
Form a linked list from the leaves of a binary tree.
@author: Ronny
"""

def formLL( root, res ):
	if root is None:
		return
		
	if root.left is None and root.right is None:
		res.append( root.data )
	else:
		formLL( root.left, res )
		formLL( root.right, res )
			
class BTNode:
	def __init__( self, **kwargs ):
		self.data = kwargs['data']
		self.left = kwargs['left']
		self.right = kwargs['right']
			
if __name__ == '__main__':
	H = BTNode( data = 'H', left = None, right = None )
	G = BTNode( data = 'G', left = H,    right = None )
	F = BTNode( data = 'F', left = None, right = G )
	D = BTNode( data = 'D', left = None, right = None )
	E = BTNode( data = 'E', left = None, right = None )
	C = BTNode( data = 'C', left = D,    right = E )
	B = BTNode( data = 'B', left = C,    right = F )	
	M = BTNode( data = 'M', left = None, right = None )
	L = BTNode( data = 'L', left = None,    right = M )
	N = BTNode( data = 'N', left = None, right = None )	
	K = BTNode( data = 'K', left = L,    right = N )	
	J = BTNode( data = 'J', left = None, right = K )		
	P = BTNode( data = 'P', left = None, right = None )	
	O = BTNode( data = 'O', left = None, right = P )	
	I = BTNode( data = 'O', left = J,    right = O )	
	A = BTNode( data = 'A', left = B,    right = I )
	
	res = []
	formLL( A, res )
	print res
	assert( res == [ 'D', 'E', 'H', 'M', 'N', 'P' ] )
	
	print "All unit tests are passed"