class Game:
    def __init__(self):
        self.events = []
        self.x = 0
        self.y = 0

    def loop(self, events):
        messages = []
        for event in events:
            if event:
                if event['type'] == 'click':
                    messages = [
                        {   
                            "type": "function",
                            "name": "drawImage",
                            "parameters": ["birdy.png",event['x'],event["y"],163,115]
                        }
                    ]
                if event['type'] == 'keydown' and event['key'] == 'c':
                    messages = [
                        {   
                            "type": "function",
                            "name": "clearRect",
                            "parameters": [0,0,700,700]
                        },
                        {
                            "type": "function",
                            "name": "beginPath",
                            "parameters": []
                        }
                    ]
        

        messages = [
            {
                "type": "function",
                "name": "drawImage",
                "parameters": ["birdy.png", self.x, self.y, 163, 115]
            }
        ]
        self.x += 1
        self.y += 1
        return messages
    

