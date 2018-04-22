# -*- coding: utf-8 -*-
"""
Find the longest nondecreasing subsequence.
@author: Ronny
"""

def findLongestSubsequence( arr ):
	max_len_subs = 0
	for idx, e in enumerate( arr ):
		temp = []	
		findLongestSubsequenceHelper( arr, idx, temp )
		if len( temp ) > max_len_subs:
			max_len_subs = len( temp )
	return max_len_subs

def findLongestSubsequenceHelper( arr, curr_idx, temp ):
	if curr_idx < len( arr ):
		if not temp or temp[-1] < arr[curr_idx]:
			temp.append( arr[curr_idx] )
		findLongestSubsequenceHelper( arr, curr_idx + 1, temp )
		
if __name__ == '__main__':	
	arr = [ 0, 8, 4, 12, 2, 10, 6, 14, 1, 9 ]
	assert( findLongestSubsequence( arr ) == 4 )
	
	print "All unit tests are passed"