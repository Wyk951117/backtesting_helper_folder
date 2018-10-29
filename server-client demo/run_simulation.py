import importlib

class multitask():
    """ testing the reload part
    """
    def __init__(self, custom_strategy=None):
        
        self.custom_strategy = custom_strategy

    def execute(self):
        strategy_module = importlib.__import__(self.custom_strategy)
        importlib.reload(strategy_module)
        test_class = strategy_module.strategy_class()



        
    def main(self): 
        self.execute()

