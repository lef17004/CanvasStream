import asyncio
import websockets
from game import Game
import json


# Global variables for WebSocket communication
messages = asyncio.Queue()
my_game = Game()
clients = [None]


async def websocket_server(websocket, path):
    clients[0] = websocket
    async for message in websocket:
        await messages.put(message)


async def game_loop():
    while True:
        await asyncio.sleep(1 / 60)  # 1/60 of a second

        processed_messages = []
        while not messages.empty():
            message = await messages.get()
            processed_messages.append(json.loads(message))

        response = my_game.loop(processed_messages)

        if response and clients[0]:
            print("response:", response)
            await clients[0].send(json.dumps(response))


async def main():
    server = await websockets.serve(websocket_server, "localhost", 8765)

    game_loop_task = asyncio.create_task(game_loop())

    await server.wait_closed()
    game_loop_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
