# Problem Statement :- 

The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.


# Sample Input :- 
price = [100, 180, 260, 310, 40, 535, 695]

# Solution :-

	n = len(price) - 1
	current =  None
	buy = None
	sell = None
	is_buy = False

	for i in range(n):
	    current = price[i]
	    if i ==0:
		if price[i+1] > current:
		    buy = current
		    is_buy = True
	    else:
		if price[i+1] > current and not is_buy:
		    buy = current
		    is_buy = True
		    
		elif price[i+1] < current and is_buy:
		    sell = current
		    print("buy :", price.index(buy), "sell :", price.index(sell))
		    is_buy = False
		else:
		    pass

	    if i== (n -1) and is_buy:
		if price[i+1] > current:
		    sell = price[i+1] 
		    print("buy :", price.index(buy), "sell :", price.index(sell))
		    is_buy = False
		

