import asyncio
import websockets
import pickle

async def talking():
	async with websockets.connect(
		#'ws://localhost:8765') as websocket:
		'ws://45.76.164.162:10') as websocket:

		#file_name = input("Input file name:\n")
		file_name = 'temp_strategy_class.py'

		await websocket.send(file_name)
		print(f">{file_name} sent")

		greeting = await websocket.recv()
		print(f"< {greeting}")

		with open(file_name, 'rb') as f:
			for data in f:
				await websocket.send(data)
		await websocket.send('END OF FILE')

		feedback = await websocket.recv()
		print(f"< {feedback}")

		request = await websocket.recv()
		print(f"< {request}")

		titles = pickle.dumps(['USDT_BTC_10sec_s'])
		await websocket.send(titles)

		feedback_figure = open('feedback_figure.jpg','wb')
		while True:
			image_slice = await websocket.recv()
			if image_slice == 'END OF FILE':
				feedback_figure.close()
				print("feedback figure received...")
				break
			else:
				feedback_figure.write(image_slice)


asyncio.get_event_loop().run_until_complete(talking())