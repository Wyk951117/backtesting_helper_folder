import random

class temp_strategy_class():
    """ a template for strategy class
    This is a template for a strategy class that should be 
    working well on backtesting.
        
    Attributes:
        index_Df: including Up, Down and RSI
        Up: measure of price increasing
        Down: measure of price decreasing
        gap: first direivative of price
        data_Df: N/A

    """

    def __init__(self):
        # create a dataframe for all the indexes you need for 
        # computing and decision making
        #self.index_Df = pd.DataFrame(index=[], columns=['Up','Down','RSI'])
        self.gap = 0
        self.Up = 0
        self.Down = 0
        self.RSI = 1

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
        for k in range(1,input_window-1):
            self.gap =input_Df.loc[k+1][input_label] - input_Df.loc[k][input_label]
            if self.gap > 0:
                self.Up += self.gap
            else:
                self.Down += self.gap
            if self.Up == 0 and self.Down == 0:
                #print ('there is neither buy nor sell.')
                return None
            else:
                self.RSI = self.Up/(self.Up + self.Down)
                #print("RSI = {}".format(self.RSI))

            # decision making process
            core = random.random()
            if self.RSI>0.5:
                #print('make a sell order')
                return 'buy'
            else:
                #print('make a buy order')
                return 'sell'

            restore_ratios()
 
    def restore_ratios():
        """
        This is an example of how you could upgrade some of your
        indexes during computing.
        """
        self.Up = 0
        self.Down = 0
        self.gap = 0
        self.RSI =1