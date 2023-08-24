class Status {
    constructor() {
        this.disconnectedStatus = document.getElementById("status");
    }

    setToConnected() {
        this.disconnectedStatus.style.display = "none";
    }

    setToDisconnected() {
        this.disconnectedStatus.style.display = "block";
    }
}