
# Simple Rule-Based Chatbot

print("Bot: Hello! I am a chatbot.")

while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hello! How are you?")
    elif "name" in user:
        print("Bot: I am a simple chatbot.")
    elif "how are you" in user:
        print("Bot: I am fine!")
    elif "bye" in user:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
