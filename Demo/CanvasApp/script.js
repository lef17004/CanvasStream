const socket = new WebSocket('ws://localhost:2020');

socket.addEventListener('open', () => {
    console.log('WebSocket connection opened');
});

socket.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);

    alert("Hello World");
});