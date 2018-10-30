import asyncio

from utils import talking
from utils import demo_talking

file_dir = 'test_strategy_files'
file_name = file_dir + 'test.py'     # change this file_name to the name of your strategy file
#handler = ''                        # change this to the transaction you want to test on
#feedback_figure_path = ''           # the path you want to save the feedback figure




# excuting client 
asyncio.get_event_loop().run_until_complete(talking(file_name,handler,feedback_figure_path))
