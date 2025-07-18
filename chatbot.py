def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    elif user_input in ["what is your name", "what's your name"]:
        return "I'm a simple chatbot!"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)

        if user_input.lower() in ["bye", "goodbye", "see you"]:
            break

# Start the chatbot
run_chatbot()
