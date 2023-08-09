import asyncio
import websockets
import webbrowser
import os
import json

current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)
path = '../CanvasApp/index.html'
webbrowser.open('file://' + os.path.realpath(path), 2)

async def echo(websocket, path):
    try:
        async for message in websocket:
            event = json.loads(message)
            print(type(event))            
            if event['type'] == 'click':
                messages = [
                    {   
                        "function": "beginPath",
                        "parameters": []
                    },
                    {   
                        "function": "lineWidth",
                        "parameters": [10]
                    },
                    {   
                        "function": "strokeStyle",
                        "parameters": ['red']
                    },
                    {   
                        "function": "rect",
                        "parameters": [event['x'], event['y'], 290, 140]
                    },
                    {   
                        "function": "stroke",
                        "parameters": []
                    }
                ]

                for return_message in messages:
                    return_string = json.dumps(return_message)
                    await websocket.send(return_string)
            print(message)
    except websockets.exceptions.ConnectionClosed:
        ...
        #await websocket.wait_closed()
        #asyncio.get_event_loop().stop()

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

