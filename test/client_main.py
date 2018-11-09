import asyncio
import websockets
import pickle

from utils import talking

strategy_dir = 'strategies/'                 # the directory to place strategy files
config_dir = 'configs/'                      # the directory to place configuration files
feedback_dir = 'feedback/'                     # the directory to place feedback figures

strategy_name = 'temp_strategy_class.py'     # the name of your strategy file
internal_config = 'internal_config.json'     # file contains parameters used to grab data from server
external_config = 'external_config.json'     # file contains parameters for strategy





asyncio.get_event_loop().run_until_complete(talking(strategy_dir, strategy_name,
                                                    internal_config, external_config, 
                                                    config_dir, feedback_dir))