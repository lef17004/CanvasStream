function main() {
    const canvas = document.getElementById("myCanvas");
    const ctx = canvas.getContext("2d");
    canvas.oncontextmenu = () => false;
    const statusImage = document.getElementById("status");

    const statusController = new Status(statusImage); 
    let websocketConnection = null;
    let eventListeners = null;

    document.addEventListener("DOMContentLoaded", () => {
        websocketConnection = new WebsocketConection(statusController, ctx);
        eventListeners = new EventListeners(canvas, websocketConnection);
    });

    ctx.imageCache = {};

    ctx.drawImg = function(imagePath, dx, dy, dWidth = null, dHeight = null) {

        if (!(imagePath in imageCache)) {
            const newImage = new Image();
            newImage.src = "/assets/" + imagePath;
            this.imageCache[imagePath] = newImage;
        }
        
        let args = [this.imageCache[imagePath], dx, dy];
        if (dWidth != null && dHeight != null) {
            args.push(dWidth);
            args.push(dHeight);
        }
    
        // Call the original drawImage method
        ctx.drawImage.apply(ctx, args);
    };


}

class Status {
    constructor(disconnectedStatus) {
        this.disconnectedStatus = disconnectedStatus;
    }

    setToConnected() {
        this.disconnectedStatus.style.display = "none";
    }

    setToDisconnected() {
        this.disconnectedStatus.style.display = "block";
    }
}

class WebsocketConection {
    constructor(status, context) {
        this.connectionStatus = status;
        this.context = context;
        this.connect();
    }

    send(object) {
        if (this.socket != null) {
            this.socket.send(JSON.stringify(object));
        }
    }

    open() {
        console.log("open");
        this.connectionStatus.setToConnected();
        this.send({
            type: "connect"
        });
    }

    message(event) {
        const eventJSON = JSON.parse(event.data);
        interpretMessage(eventJSON, this.context);
    }

    close() {
        console.log("close");
        this.send({
            type: "close"
        });
        this.socket = null;
        this.connectionStatus.setToDisconnected();
    }

    error() {
        console.log("error");
        this.socket = null;
        this.connectionStatus.setToDisconnected();
        setTimeout(() => this.connect(), 1000);
    }

    connect() {
        this.socket = new WebSocket('ws://localhost:8765');

        this.socket.addEventListener("open", (event) => {
            this.open();
        });

        this.socket.addEventListener("message", (event) => {
            this.message(event);
        });

        this.socket.addEventListener('close', (event) => {
            this.close();
        });

        this.socket.addEventListener('error', (event) => {
            this.error();
        });
    }
}

function interpretMessage(messages, ctx) {
    for (const message of messages) {
        const type = message.type;
        const name = message.name;
        const parameters = message.parameters;

        if (type == "function") {
            ctx[name].apply(ctx, parameters);
        } else if (type == "variable") {
            ctx[name] = parameters[0];
        } else if (type == "command") {

        }
    }
}

class EventListeners {
    constructor(canvas, socket) {
        this.canvas = canvas;
        this.socket = socket;
        
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
        
            this.socket.send(message);
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

            this.socket.send(message);
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
        
            this.socket.send(message);
        });
        
        this.canvas.addEventListener('mousemove', (event) => {
            const x = event.clientX - canvas.getBoundingClientRect().left;
            const y = event.clientY - canvas.getBoundingClientRect().top;
            
             const message = {
                type: "mousemove",
                 x: x,
                 y: y
             };
        
             this.socket.send(message);
        });
        
        document.addEventListener('keypress', (event) => {
            const message = {
                type: "keypress",
                key: event.key
            };
        
            this.socket.send(message);
        });
        
        document.addEventListener('keydown', (event) => {
            const message = {
                type: "keydown",
                key: event.key
            };
            
            this.socket.send(message);
        });
        
        document.addEventListener('keyup', (event) => {
            const message = {
                type: "keyup",
                key: event.key
            };
        
            this.socket.send(message);
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
        
            this.socket.send(message);
        });

        addEventListener("beforeunload", (event) => {
            const message = {
                type: "reload"
            };

            this.socket.send(message);
        });
        window.addEventListener("gamepadconnected", (event) => {
            const gamepad = event.gamepad;
            const message = {
                type: "controller",
                status: "connected",
                gamepadIndex: gamepad.index
            };
            socket.send(message);
        });

        // Handle gamepad disconnection
        window.addEventListener("gamepaddisconnected", (event) => {
            const gamepad = event.gamepad;
            const message = {
                type: "controller",
                status: "disconnected",
                gamepadIndex: gamepad.index
            };
            socket.send(message);
        });
        setInterval(() => {
            const gamepads = navigator.getGamepads();
            const message = {
                type: "controller_states"
            };

            for (const gamepad of gamepads) {
                if (gamepad) {
                    // Handle button presses
                    for (let i = 0; i < gamepad.buttons.length; i++) {
                        const button = gamepad.buttons[i];
                        const buttonState = button.pressed ? "pressed" : "unpressed";
                        message[`button${i + 1}`] = buttonState;
                    }

                    // Handle joystick axes
                    const joystickAxes = gamepad.axes.length / 2; // Divide by 2 since each joystick has 2 axes
                    for (let i = 0; i < joystickAxes; i++) {
                        const xIndex = i * 2;
                        const yIndex = i * 2 + 1;
                        const x = gamepad.axes[xIndex];
                        const y = gamepad.axes[yIndex];
                        message[`joystick${i + 1}_x`] = x;
                        message[`joystick${i + 1}_y`] = y;
                    }
                }
            }

            socket.send(message); 
        }, 16.7); // 1000 milliseconds = 1 second
                    
            }
        }

main();