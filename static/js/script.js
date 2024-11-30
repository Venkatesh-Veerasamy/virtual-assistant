document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');
    
    // Simple chat response logic
    const response = generateResponse(userInput);
    chatBox.innerHTML += `<div>User: ${userInput}</div>`;
    chatBox.innerHTML += `<div>Assistant: ${response}</div>`;
    document.getElementById('user-input').value = ''; // Clear input
});

function generateResponse(input) {
    //  responses
    const responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "good night": "Good night! Sleep well!",
        "good morning": "Good morning! Hope you have a great day!",
        "how are you": "I'm doing well, thank you! How about you?",
        "thank you": "You're welcome!",
        "what's your name": "I'm your virtual assistant.",
        "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "what can you do": "I can help with various tasks like answering questions and providing information.",
        "help me": "Sure! What do you need help with?",
        "good afternoon": "Good afternoon! How's your day going?",
        "good evening": "Good evening! How can I assist you?",
        "nice to meet you": "Nice to meet you too!",
        "what time is it": `The current time is ${new Date().toLocaleTimeString()}.`,
        "what's the weather like": "I don't have weather info right now, but you can check your local weather service.",
        "play some music": "Sure, but I need a music service integration for that!",
        "goodbye": "Take care! Goodbye!",
        
        
    };

    return responses[input.toLowerCase()] || "I'm not sure how to respond to that.";
}
