
function connectWebSocket(callback) {
    const socket = new WebSocket('ws://localhost:8765');

    socket.addEventListener('open', (event) => {
        var status = document.getElementById("status");
        status.style.backgroundColor = "green";
        callback(socket);
    });

    socket.addEventListener('message', (event) => {
        console.log('Message from server:', event.data);
    });

    socket.addEventListener('close', (event) => {
        var status = document.getElementById("status");
        status.style.backgroundColor = "red";

        // Retry connection after a delay (e.g., 1 second)
        setTimeout(() => connectWebSocket(callback), 1000);
    });

    socket.addEventListener('error', (event) => {
        var status = document.getElementById("status");
        status.style.backgroundColor = "red";

        // Retry connection after a delay (e.g., 1 second)
        setTimeout(() => connectWebSocket(callback), 1000);
    });
}

let socket = null;

connectWebSocket(function(newSocket) {
    socket = newSocket;
});

var canvas = document.getElementById("myCanvas");



canvas.addEventListener('click', (event) => {
    const x = event.clientX - canvas.getBoundingClientRect().left;
    const y = event.clientY - canvas.getBoundingClientRect().top;

    const message = {
        type: "click",
        x: x,
        y: y
    };

    socket.send(JSON.stringify(message));
});

// document.addEventListener('mousemove', (event) => {
//     const x = event.clientX;
//     const y = event.clientY;
    
//     const message = {
//         type: "mousemove",
//         x: x,
//         y: y
//     };

//     socket.send(JSON.stringify(message));
// });

canvas.addEventListener('keypress', (event) => {
    const message = {
        type: "keypress",
        key: event.key
    };

    socket.send(JSON.stringify(message));
});

document.addEventListener('keydown', (event) => {
    const message = {
        type: "keydown",
        key: event.key
    };

    socket.send(JSON.stringify(message));
});

document.addEventListener('keyup', (event) => {
    const message = {
        type: "keyup",
        key: event.key
    };

    socket.send(JSON.stringify(message));
});