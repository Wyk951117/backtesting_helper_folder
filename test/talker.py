import asyncio
import websockets
import pickle

async def talking(strategy_name, internal_config, external_config):
    async with websockets.connect(
        #'ws://localhost:8765') as websocket:
        'ws://45.76.164.162:10') as websocket:

        #file_name = input("Input file name:\n")
        #file_name = 'temp_strategy_class.py'

        async def send_file(file_name):
            # send file
            with open(file_name, 'rb') as f:
                for line in f:
                    await websocket.send(line)
                await websocket.send("END OF FILE")
        # send strategy_name greeting
        await websocket.send(strategy_name)
        print(f">{strategy_name} sent")

        # greeting from server
        greeting = await websocket.recv()
        print(f"< {greeting}")

        # send strategy file
        await send_file(strategy_name)
        print(f"{await websocket.recv()}")  # feedback from server
        
        # send internal config
        await send_file(internal_config)
        print(f"{await websocket.recv()}")

        # send external config
        await send_file(external_config)
        print(f"{await websocket.recv()}")

        # handler is not useful anymore
        """
        request = await websocket.recv()
        print(f"< {request}")

        titles = pickle.dumps(['USDT_BTC_10sec_s'])
        await websocket.send(titles)
        """

        feedback_figure = open('feedback_figure.jpg','wb')
        while True:
            info = await websocket.recv()
            if info == "image name":
                img_name = await websocket.recv()
                feedback_figure = open(img_name, 'wb')
                while True:
                    image_slice = await websocket.recv()
                    if image_slice == 'END OF FILE':
                        feedback_figure.close()
                        print("feedback figure received...")
                        break
                    else:
                        feedback_figure.write(image_slice)
            elif info == "END OF DIR":
                break


              
   
asyncio.get_event_loop().run_until_complete(talking("temp_strategy_class.py","internal_config.json","external_config.json"))