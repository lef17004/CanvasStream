class Game:
    def __init__(self):
        self.events = []
        self.x = 100
        self.y = 0
        self.grav = 0.1
        self.acceleration = 0

    def loop(self, events,ctx):
        #ctx.clearRect(0,0,700,700)
        #print('loop')
        for event in events:
            if event:
                if event["type"] == "click":
                    print("clicked!!!")
                    #ctx.drawImage("birdy.png" ,event["x"], event["y"],163,115)
                    #ctx.beginPath()
                    #ctx.lineWidth = '6'
                    #ctx.strokeStyle = "red"
                    #ctx.rect(event['x'],event['y'],290,140)
                    #ctx.stroke()

                    ctx.beginPath();
                    ctx.arc(event['x'], event['y'], 50, 0, 6.28)
                    ctx.fillStyle = "orange"
                    ctx.fill();





                if event["type"] == "keydown" and event["key"] == "c":
                    ctx.clearRect(0, 0, 700, 700)
                if event["type"] == "keydown" and event["key"] == " ":
                    self.y -= 20
                    self.acceleration = 0

        
            
        ctx.drawImage("birdy.png", self.x, self.y, 163, 115)
            
        
        self.acceleration += self.grav
        self.y += self.acceleration
