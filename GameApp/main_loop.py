from web_canvas import CanvasSubscriber, CanvasPublisher
from canvas import Canvas
class MainLoop:
    def __init__(self):
        self.subscriber = CanvasSubscriber()
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
        self.path = []
        self.ctx = Canvas()

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
                self.ctx.clearRect(0, 0, 700, 700)
                self.ctx.beginPath()
                self.path = []
                self.draw_palette()
            elif event_type == 'wheel':
                self.ctx.beginPath()
                self.path = []
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
                self.path = []
            elif event_type == 'click' and event['button'] == 0 and self.y >= 650:
                self.color = self.pallet[self.x // 70]

        if self.draw or self.erase:
            self.path.append((self.x, self.y))

            self.ctx.beginPath()
            self.ctx.strokeStyle = self.color if self.draw else 'white'
            self.ctx.lineWidth = self.lineWidth

            for point in self.path:
                self.ctx.lineTo(point[0], point[1])
            self.ctx.stroke()
            self.draw_palette()


        await self.ctx.send()

    def draw_palette(self):
        for x in range(0, 10):
            self.ctx.beginPath()
            self.ctx.fillStyle = self.pallet[x]
            self.ctx.fillRect(70 * x, 650, 70, 100)
            self.ctx.stroke()
            self.ctx.stroke()

        
            

        
