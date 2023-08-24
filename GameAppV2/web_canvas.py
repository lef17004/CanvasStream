import asyncio

class CanvasSubscriber:
    _instance = None
    events = asyncio.Queue()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CanvasSubscriber, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance
    
    async def add(self, event):
        await self.events.put(event)

    async def get(self):
        item = await self.events.get()
        return item
    
    async def get_all(self):
        all_events = []
        while not self.events.empty():
            all_events.append(await self.events.get())
        return all_events
    
    def empty(self):
        return self.events.empty()

class CanvasPublisher:
    _instance = None
    events = asyncio.Queue()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CanvasPublisher, cls).__new__(cls)
            # Additional initialization can be done here
        return cls._instance
    
    async def add(self, event):
        await self.events.put(event)

    async def get(self):
        item = await self.events.get()
        return item
    
    async def get_all(self):
        all_events = []
        while not self.events.empty():
            all_events.append(await self.events.get())
        return all_events
    
    def empty(self):
        return self.events.empty()
    
