var canvas = document.getElementById("myCanvas");
const socket = new WebSocket('ws://localhost:8765');

socket.addEventListener('open', (event) => {
});

socket.addEventListener('message', (event) => {
    
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