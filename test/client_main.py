import asyncio
import websockets
import pickle
from utils import talking


strategy_file = ''        # the name of strategy file
strategy_path = ''        # path where strategy file is 

# TODO multiple config files are possible, figure it out
config_file = ''          
config_path = ''          # path where config files are


asyncio.get_event_loop().run_until_complete(talking(strategy_file, strategy_path, config_file, config_path))
