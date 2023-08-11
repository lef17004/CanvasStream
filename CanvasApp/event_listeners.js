var canvas = document.getElementById("myCanvas");
let socket = new WebsocketConection();

canvas.addEventListener('click', (event) => {
    const x = event.clientX - canvas.getBoundingClientRect().left;
    const y = event.clientY - canvas.getBoundingClientRect().top;

    const message = {
        type: "click",
        x: x,
        y: y
    };

    socket.send(message);
});
canvas.addEventListener('mousedown', (event) => {
    const x = event.clientX - canvas.getBoundingClientRect().left;
    const y = event.clientY - canvas.getBoundingClientRect().top;

    const message = {
        type: "mousedown",
        x: x,
        y: y
    };

    socket.send(message);
});

 document.addEventListener('mousemove', (event) => {
    const x = event.clientX - canvas.getBoundingClientRect().left;
    const y = event.clientY - canvas.getBoundingClientRect().top;
    
     const message = {
        type: "mousemove",
         x: x,
         y: y
     };

    socket.send(message);
});

canvas.addEventListener('keypress', (event) => {
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