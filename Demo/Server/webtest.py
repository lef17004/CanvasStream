import asyncio
import websockets
import webbrowser
import os

path = "../Client/index.html"
webbrowser.open("file://" + os.path.realpath(path), 2)


async def echo(websocket, path):
    try:
        async for message in websocket:
            await websocket.send(message[::-1])
            print(message)
    except websockets.exceptions.ConnectionClosed:
        await websocket.wait_closed()
        asyncio.get_event_loop().stop()


start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
