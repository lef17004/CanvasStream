class Status {
    constructor() {
        this.status = document.getElementById("status")
    }

    setToConnected() {
        this.status.src = "assets/connected_status.png";
    }

    setToDisconnected() {
        this.status.src = "assets/disconnected_status.png";
    }
}