from web_canvas import CanvasSubscriber, CanvasPublisher

class MainLoop:
    def __init__(self):
        self.subscriber = CanvasSubscriber()
        self.publisher =  CanvasPublisher()

    async def main_loop(self):
        events = await self.subscriber.get_all()
        message = {}
        
        for event in events:
            print(event)
            if event['type'] == 'click':
                message = {
                    "type": "function",
                    "name": "fillRect",
                    "parameters": [event['x'], event['y'], 100, 100]
                }
                
                await self.publisher.add(message)

        
            

        
