import asyncio

class Canvas:
    def __init__(self, queue):
        self.queue = queue

    def drawImage(self, parameters):
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
