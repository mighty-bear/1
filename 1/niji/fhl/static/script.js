document.addEventListener("DOMContentLoaded", function() {
    const messageContainer = document.getElementById("message-container");
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function() {
        const message = messageInput.value;
        if (message.trim() !== "") {
            sendMessage(message);
        }
    });

    function sendMessage(message) {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/tp/chat", true);
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    const response = JSON.parse(xhr.responseText);
                    displayMessage("user", message);
                    displayMessage("system", response.system_message);
                } else {
                    console.error("Error:", xhr.statusText);
                }
            }
        };
        xhr.send("message=" + encodeURIComponent(message));
    }

    function displayMessage(sender, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", sender + "-message");
        messageElement.innerHTML = message;
        messageContainer.appendChild(messageElement);
        // Scroll to bottom
        messageContainer.scrollTop = messageContainer.scrollHeight;
    }
});
