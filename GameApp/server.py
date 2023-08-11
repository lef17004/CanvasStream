import asyncio
import websockets
from game import Game
import json


class CanvasServer:
    def __init__(self):
        self.messages = asyncio.Queue()
        self.client = None
        self.my_game = Game()

    async def server(self, websocket, path):
        self.client = websocket
        async for message in websocket:
            await self.messages.put(message)

    async def loop(self):
        while True:
            await asyncio.sleep(1 / 60)  # 1/60 of a second

            processed_messages = []
            while not self.messages.empty():
                message = await self.messages.get()
                print(message)
                processed_messages.append(json.loads(message))

            response = self.my_game.loop(processed_messages)

            if self.client and response:
                await self.client.send(json.dumps(response))

    async def start_server(self):
        server = await websockets.serve(self.server, "localhost", 8765)

        game_loop_task = asyncio.create_task(self.loop())

        await server.wait_closed()
        game_loop_task.cancel()


if __name__ == "__main__":
    server = CanvasServer()
    asyncio.run(server.start_server())
