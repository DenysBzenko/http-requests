const chatSocket = new WebSocket(
    "ws://127.0.0.1:8000/ws"
);


const messagesContainer = document.getElementById('messages');
const nameInput = document.getElementById('name');
const messageInput = document.getElementById('message');

function sendMessage() {
    if (chatSocket.readyState === WebSocket.OPEN) {
        const name = nameInput.value;
        const message = messageInput.value;

        if (name.trim() === '' || message.trim() === '') {
            alert('Please enter both name and message.');
            return;
        }
        chatSocket.send(JSON.stringify({
            'user': name,
            'text': message
        }));
        messageInput.value = '';
    } else {
        console.error("WebSocket is not open.");
    }
}

function writeToScreen(user, message) {
    const p = document.createElement('p');
    p.style.margin = '20px';
    p.style.backgroundColor = 'lightgrey';
    p.innerHTML = `<strong>${user}:</strong> ${message}`;
    messagesContainer.appendChild(p);
}

chatSocket.onmessage = function(e) {
    const message = e.data;
    const messageObject = JSON.parse(message);
    writeToScreen(messageObject.user, messageObject.text);
};

