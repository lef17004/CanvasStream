import threading
import queue
import time
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
            print("Received:", message)
            received_messages.put(message)
            
            # Echo the message back to all clients
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    finally:
        # Remove the client from the connected_clients set
        connected_clients.remove(websocket)

# Your loop function that runs 60 times a second
def loop_function(loop):
    while True:
        # Process received messages from the queue
        while not received_messages.empty():
            message = received_messages.get()
            # Process the received message here
            
        print("Inside the loop")

        # Sleep to achieve 60 times per second frequency
        time.sleep(1 / 60)

# Main function to set up websocket server and start threads
def main():
    global ws

    # Set up websocket server
    server_coroutine = websockets.serve(server, "localhost", 8765)
    
    # Start the loop function thread
    loop = asyncio.get_event_loop()
    loop_thread = threading.Thread(target=loop_function, args=(loop,))
    loop_thread.daemon = True
    loop_thread.start()

    loop.run_until_complete(server_coroutine)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        # Close the websocket connections on Ctrl+C
        for client in connected_clients:
            client.close()
        loop.stop()

if __name__ == "__main__":
    main()
