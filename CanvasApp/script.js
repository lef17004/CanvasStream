function openConnection() {
    return new WebSocket('ws://localhost:8765');
}

var canvas = document.getElementById("myCanvas");

let socket = openConnection();

socket.addEventListener('open', (event) => {
    var status = document.getElementById("status");
    status.style.backgroundColor = "green";

 });

socket.addEventListener('close', (event) => {
    var status = document.getElementById("status");
    status.style.backgroundColor = "red";
    // Attempt to reconnect every second
    setTimeout(function() {
        socket = openConnection();
    }, 1000);
});



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