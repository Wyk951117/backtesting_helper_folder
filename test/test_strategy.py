import numpy as np

def custom_strategy(temp_Df,window,label):
	U = 0
	D = 0
	RSI = 1
	for k2 in np.arange(1,window-1):
		gap = temp_Df.loc[k2+1][label] - temp_Df.loc[k2][label]
		if gap > 0:
			U += gap
		else:
			D -= gap
	if U == 0 and D == 0:
		print ('there is neither buy nor sell.')
		return None  
	else:
		RSI = U/(U+D)
		print ('RSI = %f' % RSI)
			
				### an order will be made based on the value of RSI
	
	if RSI > 0.6:
		print ('make a sell order')
		return 'buy'
	
	elif RSI <= 0.6:
		print('make a buy order')
		return 'sell'
	else:
		print ('make no order')
		return None