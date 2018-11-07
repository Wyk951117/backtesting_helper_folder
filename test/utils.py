import asyncio
import websockets
import pickle

# TODO get rid of trivial file names from this utils
# and add handlers for file names include strategy and 
# config files.
async def talking(strategy_file, strategy_path, config_file, config_path):
    async with websockets.connect(
        'ws://45.76.164.162:10') as websocket:

        # send strategy file names to shake
        # hands with server
        file_name = 'temp_strategy_class.py'
        await websocket.send(file_name)
        print(f">{file_name} sent")

        # receive feedback from server
        greeting = await websocket.recv()
        print(f"< {greeting}")

        """
        with open(file_name, 'rb') as f:
            for data in f:
                await websocket.send(data)
        await websocket.send('END OF FILE')
        """
        # send strategy file
        send_file(file_name)       

        # TODO send config files one by one
        # and perhaps delete some greetings

        feedback = await websocket.recv()
        print(f"< {feedback}")

        request = await websocket.recv()
        print(f"< {request}")

        titles = pickle.dumps(['USDT_BTC_10sec_s'])
        await websocket.send(titles)

        """
        feedback_figure = open('feedback_figure.jpg','wb')
        while True:
            image_slice = await websocket.recv()
            if image_slice == 'END OF FILE':
                feedback_figure.close()
                print("feedback figure received...")
                break
            else:
                feedback_figure.write(image_slice)
        """
        # receive feedback figures from server
        recv_figure("feedback_figure.jpg")



async def send_file(file_name):
    ## send either strategy or config 
    ## files from local to server
    with open(file_name,'rb') as f:
        for data in f:
            await websocket.send(data)
    await websocket.send('END OF FILE')

async def recv_figure(figure_name):
    ## receive feedback figures from server
    feedback_figure = open(figure_name,'wb')
    while True:
        image_slice = await websocket.recv()
        if image_slice == "END OF FILE":
            feedback_figure.close()
            print("feedback figure received,,,")
        else:
            feedback_figure.write(image_slice)
