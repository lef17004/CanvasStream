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
        this.connectionStatus.setToConnected();
    }

    message(event) {
        const eventJSON = JSON.parse(event.data);
        interpretMessage(eventJSON);
    }

    close() {
        this.socket = null;
        this.connectionStatus.setToDisconnected();
        
    }

    error() {
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

