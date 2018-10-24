import asyncio
import websockets
import pickle
import os
from myThread import mythread
import base64

async def listening(websocket,path):
	"""Receives strategy files and implement
	
	Receives strategy files (.py files) from users, save these strategy
	files to local space, start a threading for each strategy file received,
	call executing files in each threading and pass the name of file to the
	executing files so as to implement these strategies on history or realtime 
	trading records.

	Args:
		websocket: the address where this listener is executed
		path: the port of which the address this listener is executed on
	
	Returns:
		None

	PS:
		every strategy file sent to this listener should have a line says
		"END OF FILE" at the end of file.
	"""

	# request name of strategy file from client
	strategy_file_name = await websocket.recv()	#name includes ".py"
	print("strategy_file_name {} received...".format(strategy_file_name))

	feedback_1 = "{} name receivd.".format(strategy_file_name)
	await websocket.send(feedback_1)	 

	# check whether strategy file already exists, if so, delete it
	if os.path.exists(strategy_file_name):
		os.remove(strategy_file_name)
	# request body of strategy file from client
	print("Start receiving the body of {}".format(strategy_file_name))
	strategy_file = open('./'+strategy_file_name,'wb')
	
	while True:
		body_line = await websocket.recv()
		if body_line == 'END OF FILE': 	# signing the end of strategy file
			strategy_file.close()			
			print("Reaching the end of file, file saved.")
			break
		else:
			strategy_file.write(body_line)
	
	feedback_2 = "{} received.".format(strategy_file_name)
	await websocket.send(feedback_2)

	# start a thread for current strategy
	strategy_module_name = strategy_file_name	
	temp_thread = mythread(strategy_module_name)
	temp_thread.start()
	
	temp_thread.join()





listener = websockets.serve(listening,'45.76.164.162',10)
#listener = websockets.serve(listening,'localhost',8765)
print("Listening...")

asyncio.get_event_loop().run_until_complete(listener)
asyncio.get_event_loop().run_forever()
