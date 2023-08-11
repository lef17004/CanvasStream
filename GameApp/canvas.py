import asyncio

class Canvas:
    def __init__(self, queue):
        self.queue = queue

    def drawImage(self, path,x,y, width=None ,height=None):
        parameters = [path,x,y]
        if not width ==None:
            parameters.append(width)
        if not height ==None:
            parameters.append(height)
        self.queue.append(
            {
                "type": "function",
                "name": "drawImage",
                "parameters": parameters
            }
        )

    def clearRect(self,x,y,width,height):
        self.queue.append(
            {
                "type": "function",
                "name": "clearRect",
                "parameters": [x,y,width,height]
            }
        )

    def beginPath(self):
        self.queue.append(
            {
                "type": "function",
                "name": "beginPath",
                "parameters": []
            }
        )

    def set_lineWidth(self,parameters):
        self.queue.append(
            {
                "type": "attribute",
                "name": "lineWidth",
                "parameters": [parameters]
            }
        )

    lineWidth = property(None,set_lineWidth)
    def set_strokeStyle(self,parameters):
        self.queue.append(
            {
                "type": "attribute",
                "name": "strokeStyle",
                "parameters": [parameters]
            }
        )
    strokeStyle = property(None,set_strokeStyle)
    
    def rect(self,x,y,width,height):
        self.queue.append(
            {
                "type": "function",
                "name": "rect",
                "parameters": [x,y,width,height]
            }
        )

    def stroke(self):
        self.queue.append(
            {
                "type": "function",
                "name": "stroke",
                "parameters": []
            }
        )
    
    def arc(self,x, y, radius, startAngle, endAngle, counterclockwise=None):
        parameters = [x,y,radius,startAngle,endAngle]
        if not counterclockwise == None:
            parameters.append(counterclockwise)
        self.queue.append(
            {
                "type": "function",
                "name": "arc",
                "parameters": parameters
            }
        )

    def set_fillStyle(self,color):
        self.queue.append(
            {
                "type": "attribute",
                "name": "fillStyle",
                "parameters": [color]
            }
        )
    fillStyle = property(None,set_fillStyle)

    def fill(self):
        self.queue.append(
            {
                "type": "function",
                "name": "fill",
                "parameters": []
            }
        )
