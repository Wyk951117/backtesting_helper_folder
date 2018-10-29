import asyncio
import websockets

async def talking():
	async with websockets.connect(
		'ws://45.76.164.162:10') as websocket:

		file_name = 'test.py'

		await websocket.send(file_name)
		print(f">{file_name} sent")

		greeting = await websocket.recv()
		print(f"< {greeting}")

		with open('test/'+file_name, 'rb') as f:
			for data in f:
				await websocket.send(data)
		await websocket.send('END OF FILE')

		feedback = await websocket.recv()
		print(f"< {feedback}")


asyncio.get_event_loop().run_until_complete(talking())
