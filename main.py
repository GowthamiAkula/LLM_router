from classifier import classify_intent
from router import route_and_respond
from logger import log_request


def main():

    print("LLM Prompt Router")
    print("Type 'exit' to quit\n")

    while True:

        user_message = input("You: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        # Step 1: Check manual override
        if user_message.startswith("@"):

            parts = user_message.split(" ", 1)
            intent_label = parts[0][1:]

            if len(parts) > 1:
                user_message = parts[1]

            intent_data = {
                "intent": intent_label,
                "confidence": 1.0
            }

        else:
            intent_data = classify_intent(user_message)

        print("Detected Intent:", intent_data)

        # Step 2: Generate response
        response = route_and_respond(user_message, intent_data)

        # Step 3: Log request
        log_request(user_message, intent_data, response)

        # Step 4: Show response
        print("\nAssistant:", response)
        print()


if __name__ == "__main__":
    main()