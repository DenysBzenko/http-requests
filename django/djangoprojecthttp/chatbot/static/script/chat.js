const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/'
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
    const wholeMessageJSON = JSON.parse(message);
    const beMessageJSON = JSON.parse(wholeMessageJSON.yourMsg);

    console.log(beMessageJSON)
    writeToScreen(beMessageJSON.user, beMessageJSON.text)
};
