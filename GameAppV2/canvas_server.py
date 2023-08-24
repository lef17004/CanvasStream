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

# Function to start the WebSocket server and loop
def start_server_and_loop(loop):
    server_coroutine = websockets.serve(server, "localhost", 8765, loop=loop)

    canvas_server_thread = threading.Thread(target=loop.run_until_complete, args=(server_coroutine,))
    canvas_server_thread.daemon = True
    canvas_server_thread.start()

# Function to send messages to connected clients
def send_message(message):
    for client in connected_clients:
        asyncio.get_event_loop().run_until_complete(client.send(message))

# Function to get received messages from the queue
def get_received_messages():
    messages = []
    while not received_messages.empty():
        messages.append(received_messages.get())
    return messages
