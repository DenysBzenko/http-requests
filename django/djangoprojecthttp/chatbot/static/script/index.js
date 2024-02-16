const chatSocket = new WebSocket('ws://localhost:8000/ws/chat/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    displayMessage(data.message);
};

document.getElementById('send-button').addEventListener('click', function() {
    const messageInputDom = document.getElementById('message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({'message': message}));
    messageInputDom.value = '';
});

function displayMessage(message) {
    const chatMessagesDom = document.getElementById('chat-messages');
    const messageDom = document.createElement('div');
    messageDom.innerText = message;
    chatMessagesDom.appendChild(messageDom);
}
