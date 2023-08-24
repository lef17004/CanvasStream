
const supportedEvents = {
    click: "canvas",
    mousedown: "cavnas",
    mouseup: "canvas",
    mousemove: "canvas",
    wheel: "canvas",
    keypress: "document",
    keydown: "document",
    keyup: "document",
    beforeunload: "browser"
};

class EventListeners {
    constructor() {
        this.canvas = document.getElementById("myCanvas");
        
        this.canvas.addEventListener('click', (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
            const button = event.button;
        
            const message = {
                type: "click",
                x: x,
                y: y,
                button: button
            };
        
            socket.send(message);
        });

        this.canvas.addEventListener('mousedown', (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
            const button = event.button;

            const message = {
                type: "mousedown",
                x: x,
                y: y,
                button: button
            };

            socket.send(message);
        });

        canvas.addEventListener('mouseup', (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
            const button = event.button;
        
            const message = {
                type: "mouseup",
                x: x,
                y: y,
                button: button
            };
        
            socket.send(message);
        });
        
        this.canvas.addEventListener('mousemove', (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
            
             const message = {
                type: "mousemove",
                 x: x,
                 y: y
             };
        
            socket.send(message);
        });
        
        document.addEventListener('keypress', (event) => {
            const message = {
                type: "keypress",
                key: event.key
            };
        
            socket.send(message);
        });
        
        document.addEventListener('keydown', (event) => {
            const message = {
                type: "keydown",
                key: event.key
            };
            
            socket.send(message);
        });
        
        document.addEventListener('keyup', (event) => {
            const message = {
                type: "keyup",
                key: event.key
            };
        
            socket.send(message);
        });

        this.canvas.addEventListener("wheel", (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
        
            const message = {
                type: "wheel",
                x: x,
                y: y,
                deltaX: event.deltaX,
                deltaY: event.deltaY
            };
        
            socket.send(message);
        });

        addEventListener("beforeunload", (event) => {
            const message = {
                type: "reload"
            };

            socket.send(message);
        });
        
    }

    addEventListener(name) {
        if (name in supportedEvents) {
            
        }
    }
}

listeners = new EventListeners();