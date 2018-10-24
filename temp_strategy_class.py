class temp_strategy_class():
    """ a template for strategy class
    This is a template for a strategy class that should be 
    working well on backtesting.
        
    Attributes:
        index_Df: dataframe for all indexes
        input_ratio_1: ...
        input_ratio_2: ...
        input_ratio_3: ...
        input_ratio_4: ...
        interval_long: ...
        interval_short: ...
        data_Df: some dataframe intended for combine provided trading
            records and custom indexes
    """

    def __init__(self):
    	# create a dataframe for all the indexes you need for 
    	# computing and decision making
        self.index_Df = pd.DataFrame(index=[], columns=['key price',
        	'EMA short', 'EMA long', 'MACD', 'MACD signal'])
        # a bunch of parameters set by you to help computing.
        # Typically these parameters should be constant since we
        # cannot decide nor modify them for you, but you can also
        # define a function to upgrade some parameter(see upgrade_ratio_1()), 
        # just don't forget to call the function in the "compute" 
        # function since it is the only function will be called during 
        # backtesting. 
        self.input_ratio_1 = 1
        self.input_ratio_2 = 2
        self.input_ratio_3 = 3
        self.input_ratio_4 = 4   
        self.interval_long = 1
        self.interval_short = 1
        # if you want a dataframe which combines provided trading records
        # and some indexes of yourself, use the sentence below to create  
        # an empty dataframe for that or do something similar yourself.
        self.data_Df = pd.DataFrame()

    def compute(self,input_Df,input_window,input_label):
    	""" compute to decide action
    	compute using provided trading records and make
    	an action (buy/sell) based on the result.
     
        Args:
            input_Df: the dataframe containing trading records
                provided for your strategy, there might be one
                or more data streams depending on you request;
            input_window: the length of the sliding window of 
                trading records. it is now fixed, but we'll see
                whether it can be customized later;
            input_label: buy/sell label, which is also based on
                your request.
        Returns:
            action: a decision made based on the result of computing
        """

    	new_key_price = (input_Df.loc[0,'open']*input_ratio_1 + 
                     input_Df.loc[0,'high']*input_ratio_2 + 
                     input_Df.loc[0,'low'] *input_ratio_3 + 
                     input_Df.loc[0,'close']*input_ratio_4)

        # combine provided trading records and indees of yourself
        # if applicable, don't forget to uncomment in __init__()
        self.data_Df = pd.concat([input_Df, 
                        pd.DataFrame(data={'key price':[new_key_price]}), 
                        pd.DataFrame(data={'EMA short':[0]}), 
                        pd.DataFrame(data={'EMA long':[0]}), 
                        pd.DataFrame(data={'MACD':[0]}), 
                        pd.DataFrame(data={'MACD signal':[0]})], axis=1)
        
        ################################################################
        ### PS: you don't need to understand code below, just an example
        ### of some random strategy
        # calculate coefficients for different EMAs
        long_coeff = 2/(self.interval_long + 1)
        short_coeff = 2/(self.interval_short + 1)

        if self.temp_Df.shape[0] == 0:
            self.temp_Df = self.temp_Df.append(new_Df,ignore_index=True)
        
            # initialize the EMAs
            self.temp_Df.loc[0,'EMA short'] = self.temp_Df.loc[0,'key price']
            self.temp_Df.loc[0,'EMA long'] = self.temp_Df.loc[0,'key price']

        
            print ('not enough data, cannot make order')
        
        elif self.temp_Df.shape[0] < self.interval_N-1 and self.temp_Df.shape[0] != 0:
            self.temp_Df = self.temp_Df.append(new_Df,ignore_index=True)
            print ('not enough data, cannot make order')
        
        
            # update EMAs
            self.temp_Df.loc[self.temp_Df.shape[0]-1,'EMA long'] = (
                (self.temp_Df.loc[self.temp_Df.shape[0]-1,'key price'] - 
                self.temp_Df.loc[self.temp_Df.shape[0]-2,'EMA long']) * long_coeff + 
                self.temp_Df.loc[self.temp_Df.shape[0]-2,'EMA long'])
        
            self.temp_Df.loc[self.temp_Df.shape[0]-1,'EMA short'] = (
                (self.temp_Df.loc[self.temp_Df.shape[0]-1,'key price'] - 
                self.temp_Df.loc[self.temp_Df.shape[0]-2,'EMA short']) * short_coeff + 
                self.temp_Df.loc[self.temp_Df.shape[0]-2,'EMA short'])
        
            # update MACD
            self.temp_Df.loc[self.temp_Df.shape[0]-1,'MACD'] = (
                self.temp_Df.loc[self.temp_Df.shape[0]-1,'EMA short'] - 
                self.temp_Df.loc[self.temp_Df.shape[0]-1,'EMA long'])
        
            # update MACD signal
            self.temp_Df.loc[self.temp_Df.shape[0]-1,'MACD signal'] = (
                self.temp_Df.loc[0:self.temp_Df.shape[0]-1,'MACD'].sum/self.temp_Df.shape[0])
        


        elif self.temp_Df.shape[0] == self.interval_N:
            self.temp_Df = self.temp_Df.drop(0)
            self.temp_Df = self.temp_Df.append(new_Df,ignore_index=True)
        
        
            # update EMA
            self.temp_Df.loc[self.interval_N-1,'EMA long'] = (
                (self.temp_Df.loc[self.interval_N-1,'key price'] - 
                 self.temp_Df.loc[self.interval_N-2,'EMA long']) * long_coeff + 
                self.temp_Df.loc[self.interval_N-2,'EMA long'])
        
            self.temp_Df.loc[self.interval_N-1,'EMA short'] = (
                (self.temp_Df.loc[self.interval_N-1,'key price'] - 
                self.temp_Df.loc[self.interval_N-2,'EMA short']) * short_coeff + 
                self.temp_Df.loc[self.interval_N-2,'EMA short'])
        
            # update MACD
            self.temp_Df.loc[self.interval_N-1,'MACD'] = (
                self.temp_Df.loc[self.interval_N-1,'EMA short'] - 
                self.temp_Df.loc[self.interval_N-1,'EMA long'])
        
            # update MACD signal
            self.temp_Df.loc[self.interval_N-1,'MACD signal'] = (
                self.temp_Df.loc[0:self.interval_N-1,'MACD'].sum/self.interval_N)
    
        # This is MACD signal
        beacon = self.temp_Df.loc[self.interval_N-1,'MACD signal']
        ##########################################################################
        # if your would upgrade index during computing
        upgrade_ratio_1()

        if beacon < -1:
        	return "buy"
        elif beacon >1:
        	return "sell"
        else:
        	return None
 
    def upgrade_ratio_1():
    	"""
    	This is an example of how you could upgrade some of your
    	indexes during computing.
    	"""
    	if len(self.data_Df) > 50:
    		self.input_ratio_1 += 1