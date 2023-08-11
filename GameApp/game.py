class Game:
    def __init__(self):
        self.events = []
        self.x = 100
        self.y = 0
        self.grav = 0.1
        self.acceleration = 0

    def loop(self, events):
        # print('loop')
        if events:
            print(events)
        messages = [
            {"type": "function", "name": "clearRect", "parameters": [0, 0, 700, 700]}
        ]
        for event in events:
            if event:
                if event["type"] == "click":
                    messages = [
                        {
                            "type": "function",
                            "name": "drawImage",
                            "parameters": [
                                "birdy.png",
                                event["x"],
                                event["y"],
                                163,
                                115,
                            ],
                        }
                    ]
                if event["type"] == "keydown" and event["key"] == "c":
                    messages = [
                        {
                            "type": "function",
                            "name": "clearRect",
                            "parameters": [0, 0, 700, 700],
                        },
                        {"type": "function", "name": "beginPath", "parameters": []},
                    ]
                if event["type"] == "keydown" and event["key"] == " ":
                    self.y -= 20
                    self.acceleration = 0

        messages += [
            {
                "type": "function",
                "name": "drawImage",
                "parameters": ["birdy.png", self.x, self.y, 163, 115],
            }
        ]
        self.acceleration += self.grav
        self.y += self.acceleration
        # return []
        return messages
