const socket = new WebSocket("ws://localhost:8000/ws");

const status = document.getElementById("status");
const messages = document.getElementById("messages");
const form = document.getElementById("chat-form");
const input = document.getElementById("message-input");

socket.onopen = function () {
    status.textContent = "Connected";
    status.className = "connected";
};

socket.onmessage = function (event) {
    const message = document.createElement("div");
    message.textContent = "Server: " + event.data;
    message.className = "received";
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
};

socket.onclose = function () {
    status.textContent = "Disconnected";
    status.className = "disconnected";
};

socket.onerror = function () {
    status.textContent = "Connection error";
    status.className = "disconnected";
};

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const text = input.value;

    if (text.trim() === "" || socket.readyState !== WebSocket.OPEN) {
        return;
    }

    socket.send(text);

    const message = document.createElement("div");
    message.textContent = "You: " + text;
    message.className = "sent";
    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;
    input.value = "";
});
