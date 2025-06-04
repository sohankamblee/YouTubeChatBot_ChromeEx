document.addEventListener("DOMContentLoaded", function () {
    let videoId = "";

    // Function to extract video ID from current tab's URL
    function extractVideoIdFromUrl(url) {
        const urlObj = new URL(url);
        return urlObj.searchParams.get("v");
    }

    // Fetch current tab's video ID
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        videoId = extractVideoIdFromUrl(tabs[0].url);
    });

    // Get DOM elements safely
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatWindow = document.getElementById("chat-window");

    if (!chatForm || !userInput || !chatWindow) {
        console.error("Missing chat form elements in popup.html.");
        return;
    }

    // Handle user input loop
    chatForm.addEventListener("submit", async function (e) {
        e.preventDefault();
        const input = userInput.value.trim();
        if (!input) return;

        appendMessage("You", input);

        if (input.toLowerCase() === "exit") {
            appendMessage("Bot", "Chatbot session ended. Closing chat...");
            userInput.disabled = true;
            setTimeout(() => {
                window.close();
            }, 2000);
            return;
        }

        try {
            const response = await fetch("http://localhost:8000/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    video_id: videoId,
                    user_input: input
                })
            });

            const data = await response.json();
            appendMessage("Bot", data.response || data.error || "No response received from server.");
        } catch (err) {
            appendMessage("Bot", "Error contacting server.");
        }

        userInput.value = "";
    });

    function appendMessage(sender, text) {
        const msg = document.createElement("div");
        msg.className = "message";
        msg.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatWindow.appendChild(msg);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }
});
