async function sendMessage() {
    const input = document.getElementById("ingredientInput");
    const chatBox = document.getElementById("chatBox");

    const userText = input.value.trim();
    if (!userText) return;

    // User message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = userText;
    chatBox.appendChild(userDiv);

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // API call
    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `ingredient=${encodeURIComponent(userText)}`
    });

    const data = await response.json();

    // Bot message
    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = "🍲 " + data.recipe;
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}
