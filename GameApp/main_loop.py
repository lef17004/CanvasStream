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
        self.x = 0
        self.y = 0
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
        events = await self.subscriber.get_all()

        for event in events:
            if not event:
                continue

            event_type = event['type']
            if event_type == "mousemove":
                self.prevx = self.x
                self.prevy = self.y
                self.x = event['x']
                self.y = event['y']
            elif event_type == "keydown" and event["key"] == "c":
                self.ctx.clearRect(0, 0, 700, 650)
                self.draw_palette()
            elif event_type == 'wheel':
                self.ctx.beginPath()
                self.path.clear()
                if event['deltaY'] < 0:
                    self.lineWidth += 1
                else:
                    if self.lineWidth > 1:
                        self.lineWidth -= 1
            elif event_type == "mousedown":
                button = event['button']
                if button == 0:
                    self.draw = True
                elif button == 2:
                    self.erase = True
                self.prevx = self.x
                self.prevy = self.y
                self.x = event['x']
                self.y = event['y']
            elif event_type == "mouseup":
                button = event['button']
                if button == 0:
                    self.draw = False
                elif button == 2:
                    self.erase = False
                self.ctx.beginPath()
                self.path.clear()
            elif event_type == 'click' and event['button'] == 0 and self.y >= 650:
                self.color = self.pallet[self.x // 70]

            self.process_draw_erase()
        
        await self.ctx.send()

    def process_draw_erase(self):
        if self.draw or self.erase:
            if not self.path:
                self.ctx.beginPath()
                self.ctx.arc(self.x, self.y, self.lineWidth/2, 0, 6.28)
                self.ctx.fillStyle = self.color if self.draw else 'white'
                self.ctx.fill()

            self.path.append((self.x, self.y))
            if len(self.path) > 3:
                self.path.popleft()

            self.ctx.beginPath()
            self.ctx.strokeStyle = self.color if self.draw else 'white'
            self.ctx.lineWidth = self.lineWidth

            for point in self.path:
                self.ctx.lineTo(point[0], point[1])
            self.ctx.stroke()
            self.draw_palette()

    def draw_palette(self):
        for x in range(len(self.pallet)):
            self.ctx.fillStyle = self.pallet[x]
            self.ctx.fillRect(70 * x, 650, 70, 100)
        
        self.ctx.stroke()
