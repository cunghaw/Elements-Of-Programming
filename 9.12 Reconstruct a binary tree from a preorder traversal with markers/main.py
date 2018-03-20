# -*- coding: utf-8 -*-
"""
Reconstruct a binary tree from an inorder traversal sequence and a preorder traversal sequence.
@author: Ronny
"""

def constructTree( preorder, inorder ):
	return constructTreeHelper( preorder, 0, len( preorder ) -1, inorder, 0, len( inorder ) -1 )
	
def constructTreeHelper( preorder, pre_low_idx, pre_high_idx, inorder, in_low_idx, in_high_idx ):
	if pre_low_idx > pre_high_idx or in_low_idx > in_high_idx:
		return None
	else:
		root = preorder[pre_low_idx]
		size_left_tree = inorder.index( root ) - in_low_idx
		size_right_tree = in_high_idx - inorder.index( root )
		return BinaryTreeNode( root, 
							   constructTreeHelper( preorder, pre_low_idx + 1, pre_low_idx + size_left_tree, inorder, in_low_idx, inorder.index( root ) - 1 ),
							   constructTreeHelper( preorder, pre_high_idx - size_right_tree + 1, pre_high_idx, inorder, inorder.index( root ) + 1, in_high_idx ) )
			
class BinaryTreeNode:
	def __init__( self, data, left = None, right = None ):
		self.data = data
		self.left = left
		self.right = right
			
def collectPreTraversalNode( root ):
	if not root:
		return []

	l_res = collectPreTraversalNode( root.left )
	r_res = collectPreTraversalNode( root.right )
	return [ root.data ] + l_res + r_res
		
def collectInTraversalNode( root ):
	if not root:
		return []
	
	l_res = collectInTraversalNode( root.left )
	r_res = collectInTraversalNode( root.right )
	return l_res + [ root.data ] + r_res
			
if __name__ == '__main__':
	left = BinaryTreeNode( 2 )
	right = BinaryTreeNode( 3 )
	root = BinaryTreeNode( 1, left, right )
	
	# Test pre-order / in-order traversal
	assert( collectPreTraversalNode( root ) == [ 1, 2, 3 ] )
	assert( collectInTraversalNode( root )  == [ 2, 1, 3 ] )
	
	root = constructTree( ['H','B','F','E','A','C','D','G','I'], ['F','B','A','E','H','C','D','I','G'] )
	assert( collectPreTraversalNode( root ) == ['H','B','F','E','A','C','D','G','I'] )
	assert( collectInTraversalNode( root )  == ['F','B','A','E','H','C','D','I','G'] )	
	
	print "All unit tests are passed"