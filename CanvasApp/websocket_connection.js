class WebsocketConection {
    constructor() {
        this.connectionStatus = new Status();
        this.context = document.getElementById("myCanvas").getContext("2d");
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
        interpretMessage(eventJSON);
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

let socket = null;

document.addEventListener("DOMContentLoaded", () => {
    socket = new WebsocketConection();
});