def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi"]:
        return "Hi!"
    elif user_input in ["how are you", "how r u"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

def run_chatbot():
    print(" Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    run_chatbot()
