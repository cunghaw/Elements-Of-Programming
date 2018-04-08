# -*- coding: utf-8 -*-
"""
Build a minimum height BST from a sorted array.
@author: Ronny
"""

from __future__ import print_function
from collections import deque

class Node:
	def __init__( self, **kwargs ):
		self.data = kwargs['data']
		self.left = kwargs['left']
		self.right = kwargs['right']
	
def constructTree( array ):
	return constructTreeHelper( array, 0, len( array ) -1 )
	
def constructTreeHelper( array, start, end ):
	if start <= end:
		mid = ( start + end ) / 2
		root = Node( data = array[mid], left = constructTreeHelper( array, start, mid - 1 ), right = constructTreeHelper( array, mid + 1, end ) )
		return root
	else:
		return None

def calcHeightTree( root ):
	if root is None:
		return 0
	else:
		return 1 + max( calcHeightTree( root.left ), calcHeightTree( root.right ) )

def printTree( root ):
	currentLevel = deque([])
	currentLevel.append( root )
	height = calcHeightTree( root ) + 2
	nextLevel = deque([])
	while currentLevel:
		node = currentLevel.popleft()
		print( "".join( [' '] * height ) + "{0}".format( node.data ), end = '' )
		if node.left is not None:
			nextLevel.append( node.left )		
		if node.right is not None:
			nextLevel.append( node.right )
		if not currentLevel:
			currentLevel = nextLevel
			nextLevel = deque([])
			height = height / 2 + 1
			print('')

if __name__ == '__main__':
	sortedArray = [1,2,3,4,5,6,7]
	root = constructTree( sortedArray )
	printTree( root )
	
	print( "All unit tests are passed" )