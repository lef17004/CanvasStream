class Game:
    def __init__(self):
        self.events = []
        self.x = 0
        self.y = 0
        self.grav = 0.1
        self.acceleration = 0
        self.draw = False
        self.erase = False
        self.lineWidth=5
        self.color = "black"
        self.pallet = ['black','Red','Blue','Green','Yellow','Pink','Grey','Purple','orange','brown']
        self.prevx = 0
        self.prevy = 0
        self.path = []

    def loop(self, events,ctx):

        #ctx.clearRect(0,0,700,700)
        #print('loop')
        for event in events:
            if event:
                if event["type"] == "mousedown"and event['button']==0:
                    self.draw = True
                    self.prevx = self.x
                    self.prevy = self.y
                    self.x = event['x']
                    self.y = event['y']
                if event["type"] == "mousemove" :
                    self.prevx = self.x
                    self.prevy = self.y
                    self.x = event['x']
                    self.y = event['y']
                if event["type"] == "keydown" and event["key"] == "c":
                    ctx.clearRect(0, 0, 700, 700)
                    ctx.beginPath()
                    self.path = []
                if event['type'] == "mouseup"and event['button']==0:
                    self.draw = False
                    ctx.beginPath()
                    self.path = []
                if event['type'] == 'wheel':
                    ctx.beginPath()
                    self.path = []
                    print("scrolling")
                    if event['deltaY'] < 0:
                        print("increasing")
                        self.lineWidth += 1  # Increase line width
                    else:
                        print("Decreasing")
                        if (self.lineWidth>1):
                            self.lineWidth -= 1
                if event["type"] == "mousedown"and event['button']==2:
                    self.erase = True
                    self.prevx = self.x
                    self.prevy = self.y
                    self.x = event['x']
                    self.y = event['y']
                if event['type'] == "mouseup"and event['button']==2:
                    self.erase = False
                    ctx.beginPath()
                    self.path = []
                if event['type'] == 'click' and event['button'] ==0 and self.y>=650:
                    self.color = self.pallet[self.x//70]

                
        if self.draw:
            # Add the current point to the path
            self.path.append((self.x, self.y))

            ctx.beginPath()
            ctx.strokeStyle = self.color
            ctx.lineWidth = self.lineWidth
            
            # Connect all points in the path to create a continuous line
            for point in self.path:
                ctx.lineTo(point[0], point[1])
            ctx.stroke()
        if self.erase:
            # Similar to drawing, maintain a separate path for erasing
            self.path.append((self.x, self.y))

            ctx.beginPath()
            ctx.strokeStyle = 'white'
            ctx.lineWidth = self.lineWidth

            for point in self.path:
                ctx.lineTo(point[0], point[1])
            ctx.stroke()
        for x in range(0,10):
            ctx.beginPath()
            ctx.fillStyle = self.pallet[x]
            ctx.fillRect(70*x, 650, 70, 100);  
            ctx.stroke()
        

        
            
        
            
        

