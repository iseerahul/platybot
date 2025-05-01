from platy import ask_platy

print("Welcome to Platy CLI! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Platy: Goodbye!")
        break
    reply = ask_platy(user_input)
    print(f"Platy: {reply}")
