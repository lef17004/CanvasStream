import asyncio
import websockets
import json
from web_canvas import CanvasSubscriber, CanvasPublisher
from main_loop import MainLoop
import time

class CanvasServer:
    def __init__(self):
        self.messages = asyncio.Queue()
        self.client = None
        self.events = CanvasSubscriber()
        self.to_client_events = CanvasPublisher()
        self.main = MainLoop()
        self.frame_time = 1 / 60  # Target frame time in seconds


    async def server(self, websocket, path):
        
        self.client = websocket
        async for message in websocket:
            message_dict = json.loads(message)
            if message_dict['type'] == "reload":
                print('reload')
                self.client = None
            print(message)
            await self.events.add(json.loads(message))

    async def loop(self):
        while True:
            start_time = time.time()

            await self.main.main_loop()

            to_send_messages = await self.to_client_events.get_all()
            if to_send_messages:
                #print(to_send_messages)
                ...

            if self.client and to_send_messages:
                await self.client.send(json.dumps(to_send_messages))

            elapsed_time = time.time() - start_time
            sleep_time = self.frame_time - elapsed_time
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)
            else:
                print("Frame took too long to process")
            

    async def start_server(self):
        server = await websockets.serve(self.server, "localhost", 8765)

        game_loop_task = asyncio.create_task(self.loop())

        await server.wait_closed()
        game_loop_task.cancel()


if __name__ == "__main__":
    server = CanvasServer()
    asyncio.run(server.start_server())