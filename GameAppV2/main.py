import time
import asyncio
import canvas_server

def main():
    loop = asyncio.get_event_loop()

    # Start the WebSocket server and associated loop in a separate thread
    canvas_server.start_server_and_loop(loop)

    while True:
        print("Inside the main loop")

        # Send a message to clients
        canvas_server.send_message("Hello from main.py")

        # Get received messages from canvas_server
        received_messages = canvas_server.get_received_messages()
        for message in received_messages:
            print("Received:", message)

        time.sleep(1)  # Sleep for 1 second

if __name__ == "__main__":
    main()
