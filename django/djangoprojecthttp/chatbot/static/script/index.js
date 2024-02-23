const chatSocket = new WebSocket(
    "ws://127.0.0.1:8000/ws"
);

console.log('Hello from myscript.js!');
const output = document.querySelector("#output");


function writeToScreen(message) {
    const li = document.createElement('p');
    li.style.margin = '20px';
    li.style.backgroundColor = 'lightgrey';
    li.textContent = message;
    output.appendChild(li);
}


chatSocket.onopen = function(e) {
    console.log('opened connection');
    let pingInterval = setInterval(() => sendMessage("msg from client"), 100);
    setTimeout(() => clearInterval(pingInterval), 2000)
};

chatSocket.onmessage = function(e) {
    const message = e.data;
    console.log(message)
    writeToScreen(message)
    // Handle incoming message
};


chatSocket.onerror = function(e) {
    console.error('Error appeared', e);
};
chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly', e);
};

function sendMessage(message) {
    chatSocket.send(message);
}

function handleClick() {
    sendMessage('Button clicked! Ping!')
}
