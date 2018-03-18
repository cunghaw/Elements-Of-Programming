# -*- coding: utf-8 -*-
"""
Find the maximum profit of stock prices data.
@author: Ronny
"""

def getMaximumProfit ( array ):

	last_price = array[0]
	diff_array = []
	for curr_price in array[1:]:
		diff_array.append( curr_price - last_price )
		last_price = curr_price

	max_profit = 0
	profit_so_far = 0
	curr_profit = 0
	for diff in diff_array:
		if diff + profit_so_far > 0:
			profit_so_far += diff
		else:
			profit_so_far = 0
		if max_profit < profit_so_far:
			max_profit = profit_so_far

	return max_profit
	
if __name__ == '__main__':
	assert( getMaximumProfit( [ 310, 315, 275, 295, 260, 270, 290, 230, 255, 250 ] ) == 30 )
	assert( getMaximumProfit( [ 300, 200, 100, 50, 10 ] ) == 0 )
	assert( getMaximumProfit( [ 0, 10, 100, 200, 300  ] ) == 300 )	
	print "All unit tests are passed"