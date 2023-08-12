import asyncio
import websockets
import json
from web_canvas import CanvasSubscriber, CanvasPublisher
from main_loop import MainLoop

class CanvasServer:
    def __init__(self):
        self.messages = asyncio.Queue()
        self.client = None
        self.events = CanvasSubscriber()
        self.to_client_events = CanvasPublisher()
        self.main = MainLoop()

    async def server(self, websocket, path):
        
        self.client = websocket
        async for message in websocket:
            await self.events.add(json.loads(message))

    async def loop(self):
        while True:
            await asyncio.sleep(1 / 60)  # 1/60 of a second
            await self.main.main_loop()

            to_send_messages = await self.to_client_events.get_all()
            if to_send_messages:
                print(to_send_messages)

            if self.client and to_send_messages:
                await self.client.send(json.dumps(to_send_messages))
            

    async def start_server(self):
        server = await websockets.serve(self.server, "localhost", 8765)

        game_loop_task = asyncio.create_task(self.loop())

        await server.wait_closed()
        game_loop_task.cancel()


if __name__ == "__main__":
    server = CanvasServer()
    asyncio.run(server.start_server())