import threading
import queue
import websockets
import asyncio

# Global variable to store the list of connected clients
connected_clients = set()

# Create a thread-safe queue to store received messages
received_messages = queue.Queue()

# Function to receive messages over the websocket connection
async def server(websocket, path):
    global connected_clients
    # Add the client to the connected_clients set
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            received_messages.put(message)
    finally:
        # Remove the client from the connected_clients set
        connected_clients.remove(websocket)

def start_websocket_server():
    server_coroutine = websockets.serve(server, "localhost", 8765)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(server_coroutine)
    loop.run_forever()

def send_message(message):
    for client in connected_clients:
        asyncio.get_event_loop().run_until_complete(client.send(message))
        
def get_received_messages():
    messages = []
    while not received_messages.empty():
        messages.append(received_messages.get())
    return messages
