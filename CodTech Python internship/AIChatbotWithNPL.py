import nltk
from nltk.chat.util import Chat, reflections

# Define conversation patterns
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am an AI Chatbot created using Python and NLP."]
    ],
    [
        r"how are you ?",
        ["I'm doing great! How about you?"]
    ],
    [
        r"what can you do ?",
        ["I can answer simple questions and chat with you using NLP."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a nice day 😊"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn’t understand that. Can you rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

print("🤖 AI Chatbot is running...")
print("Type 'bye' to exit.\n")

# Start chat
chatbot.converse