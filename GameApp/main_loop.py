from collections import deque
from web_canvas import CanvasSubscriber, CanvasPublisher
from canvas import Canvas

class MainLoop:
    def __init__(self):
        self.subscriber = CanvasSubscriber()
        self.ctx = Canvas()
        self.initialize_state()

    def initialize_state(self):
        self.events = []
        self.x = 350
        self.y = 350
        self.grav = 0.1
        self.acceleration = 0
        self.draw = False
        self.erase = False
        self.lineWidth = 5
        self.color = "black"
        self.pallet = ['black', 'Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Grey', 'Purple', 'orange', 'brown']
        self.prevx = 0
        self.prevy = 0
        self.path = deque()

    async def main_loop(self):
        self.ctx.clearRect(0, 0, 700, 700)
        events = await self.subscriber.get_all()

        for event in events:
            if not event:
                continue

            event_type = event['type']
            if event_type == "controller_states":
                if 'joystick1_x' in event and 'joystick1_y' in event:
                    x = event['joystick1_x']
                    y = event['joystick1_y']
                    print(f"Joystick 1 X: {x}, Y: {y}")
                    self.x+= x*5
                    self.y+= y*5
                    print(f"x: {self.x} y: {self.y}")

                
        self.ctx.beginPath()
        self.ctx.lineWidth = "1"
        self.ctx.arc(self.x, self.y, 15, 0, 6.28)
        self.ctx.stroke()
        await self.ctx.send()
