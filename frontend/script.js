document.addEventListener("DOMContentLoaded", () => {
  const chatbotBtn = document.getElementById("chatbot-button");
  const chatWindow = document.getElementById("chat-window");
  const closeBtn = document.getElementById("close-btn");
  const sendBtn = document.getElementById("send-btn");
  const userInput = document.getElementById("user-input");
  const chatMessages = document.getElementById("chat-messages");

  // Show chat window
  chatbotBtn.addEventListener("click", () => {
    chatWindow.classList.remove("chat-hidden");
    chatWindow.classList.add("chat-visible");
    chatbotBtn.style.display = "none";
  });

  // Hide chat window
  closeBtn.addEventListener("click", () => {
    chatWindow.classList.remove("chat-visible");
    chatWindow.classList.add("chat-hidden");
    chatbotBtn.style.display = "flex";
  });

  // Send message on click
  sendBtn.addEventListener("click", sendMessage);

  // Send message on Enter
  userInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  });

  function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage("user-message", "You: " + message);
  userInput.value = "";

  // Show typing indicator
  const typingDiv = document.createElement("div");
  typingDiv.className = "typing-indicator";
  typingDiv.innerHTML = `<span></span><span></span><span></span>`;
  chatMessages.appendChild(typingDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;

  // Simulate 2-second delay then respond
  setTimeout(() => {
    typingDiv.remove(); // Remove typing indicator

    // Simulated or fetched response
    fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    })
    .then(res => res.json())
    .then(data => {
      appendMessage("bot-message", "Broom: " + data.response);
    })
    .catch(() => {
      appendMessage("bot-message", "Broom: Sorry, something went wrong.");
    });
  }, 1000); // 2 seconds
}

  function appendMessage(className, text) {
    const div = document.createElement("div");
    div.className = className;
    div.innerText = text;
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }
});
