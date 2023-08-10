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
                        "type": "function",
                        "name": "drawImage",
                        "parameters": ["birdy.png",event['x'],event["y"],100,100]
                    }
                ]
            if event['type'] == 'keydown':
                messages = [
                    {   
                        "type": "function",
                        "name": "clearRect",
                        "parameters": [0,0,700,700]
                    },
                    {
                        "type": "function",
                        "name": "beginPath",
                        "parameters": []
                    }
                ]


        
            return_string = json.dumps(messages)
            await websocket.send(return_string)
            print(message)
    except websockets.exceptions.ConnectionClosed:
        ...
        #await websocket.wait_closed()
        #asyncio.get_event_loop().stop()

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

