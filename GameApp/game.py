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
                if 'joystick2_x' in event and 'joystick2_y' in event:
                    x2 = event['joystick2_x']
                    y2 = event['joystick2_y']
                    if y2 != 0:
                        if self.lineWidth>=1 or y2<0:
                            self.lineWidth -= y2
                            self.path.append((self.x, self.y,'new',self.lineWidth))
                if 'button2' in event:
                    if event['button2'] == 'pressed':
                        print("PRESSED")
                        self.draw = True
                    elif event['button2'] == 'unpressed':
                        self.path.append((self.x, self.y,'new',self.lineWidth))
                        self.draw = False
                        #self.path.clear()
                if 'button3' in event:
                    if event['button3'] == 'pressed':
                        self.ctx.clearRect(0, 0, 700, 700)
                        self.path.clear()
                        



        self.process_draw_erase()
        for x in range(len(self.pallet)):
            self.ctx.fillStyle = self.pallet[x]
            self.ctx.fillRect(70 * x, 650, 70, 100)
        self.ctx.beginPath()
        self.ctx.lineWidth = 1
        self.ctx.arc(self.x, self.y, self.lineWidth/2, 0, 6.28)
        self.ctx.stroke()
        await self.ctx.send()

    def process_draw_erase(self):
        #print('AAA')
        #if self.draw or self.erase:
        #print("BBB")
        #if not self.path:
        #    #print("CCC")
        #    self.ctx.beginPath()
        #    self.ctx.arc(self.x, self.y, self.lineWidth/2, 0, 6.28)
        #    self.ctx.fillStyle = self.color
        #    self.ctx.fill()
        if self.draw:
            self.path.append((self.x, self.y,'continue',self.lineWidth))
            #if len(self.path) > 3:
            #    self.path.popleft()
                #print("DDD")

        self.ctx.beginPath()
        self.ctx.strokeStyle = self.color
        self.ctx.lineWidth = self.lineWidth
        #print("EEE")
        for point in self.path:
            if point[2] == 'continue':
                self.ctx.lineTo(point[0], point[1])
            else:
                self.ctx.stroke()
                self.ctx.beginPath()
                self.ctx.strokeStyle = self.color
                self.ctx.lineWidth = point[3]
                #self.ctx.lineTo(point[0], point[1])
        self.ctx.stroke()
