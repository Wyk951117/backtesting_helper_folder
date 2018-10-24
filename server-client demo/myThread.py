import threading
from run_simulation import multitask

class mythread(threading.Thread):
	""" called by listener.py and implements strategy modules

	This class is called by server.py, receiving the name of
	test modules generated from test files and execute
	simulation part so as to implement various strategies

	Attributes:
		module: the name of module passed from server.py.
	"""
	def __init__(self, module):
		threading.Thread.__init__(self)
		self.module = module


	def run(self):
		module_name =self.module[:-3]	#get rid of ".py"
		cur_task = multitask(module_name)
		cur_task.main()
		print("current task terminated")
