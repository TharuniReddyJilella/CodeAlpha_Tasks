def chatbot_response(user_message):

    user_message = user_message.lower()

    if user_message == "python":
        return (
            "Python is a high-level programming language known for its "
            "simple syntax and readability. It is widely used in Artificial Intelligence, "
            "Data Science, Web Development, and Automation."
        )

    elif user_message == "java":
        return (
            "Java is an object-oriented programming language widely used "
            "for enterprise applications and Android development."
        )

    elif user_message == "dsa":
        return (
            "DSA stands for Data Structures and Algorithms. "
            "It helps improve problem-solving and coding skills."
        )

    elif user_message == "dbms":
        return (
            "DBMS stands for Database Management System. "
            "It is used to store and manage data efficiently."
        )

    elif user_message == "jokes":
        return (
            "Why do programmers prefer dark mode? "
            "Because light attracts bugs!"
        )

    elif user_message == "bored":
        return (
            "You could try learning a new skill, reading a book, "
            "watching a good movie, or solving coding challenges."
        )

    elif user_message in ["movies", "suggest movies"]:
        return (
            "Here are some movie recommendations:\n"
            "1. Salaar\n"
            "2. RRR\n"
            "3. Sita Ramam\n"
            "4. 777 Charlie\n"
            "5. Kalki 2898 AD"
        )

    elif user_message == "books":
        return (
            "Here are some good books:\n"
            "1. Wings of Fire\n"
            "2. The Race of My Life\n"
            "3. Playing It My Way\n"
            "4. Life's Amazing Secrets"
        )

    elif user_message in ["motivation", "motivate me"]:
        return (
            "Success is the sum of small efforts repeated every day."
        )

    elif user_message == "how are you":
        return "I'm doing well, thank you for asking!"

    else:
        return (
            "I'm sorry, I don't have information on that topic yet.\n"
            "I can help you with:\n"
            "- Python\n"
            "- Java\n"
            "- DSA\n"
            "- DBMS\n"
            "- Movies\n"
            "- Books\n"
            "- Jokes\n"
            "- Motivation"
        )


print("=" * 45)
print("         WELCOME TO SMARTBOT")
print("=" * 45)

user_input = input("\nYou: ").lower()

if user_input in ["hello", "hi", "hai"]:

    print("\nBot: Hello! It's a pleasure to meet you.")
    print("Bot: How are you doing today?")

    mood = input("You: ").lower()

    if mood in ["bad", "sad", "not good", "upset"]:
        print("\nBot: I'm sorry to hear that.")
        print("Bot: I hope things get better soon. Stay positive and take care of yourself.")
    else:
        print("\nBot: That's wonderful to hear!")

    print("\nBot: May I know your name?")

    user_name = input("You: ").title()

    print(f"\nBot: Nice to meet you, {user_name}.")
    print("Bot: How may I assist you today?")

    follow_up_messages = [
        "Is there anything else I can help you with?",
        "I'd be happy to assist you further. Do you have another question?",
        "I'm glad our conversation has been helpful. What else would you like to know?",
        "It's a pleasure talking with you. Is there anything more I can assist you with today?",
        "Thank you for your interesting questions. Do you have anything else you'd like to ask?"
    ]

    conversation_count = 0

    while True:

        user_query = input(f"\n{user_name}: ").lower()

        if user_query in ["bye", "goodbye", "ok bye", "no", "exit", "quit"]:

            print("\nBot: Thank you for spending your time with me.")
            print("Bot: I truly enjoyed our conversation.")
            print("Bot: I hope I was able to help you today.")
            print(f"Bot: Have a wonderful day, {user_name}. Goodbye!")

            break

        response = chatbot_response(user_query)

        print("\nBot:", response)

        if conversation_count < len(follow_up_messages):
            print("\nBot:", follow_up_messages[conversation_count])
        else:
            print("\nBot: I'm always here whenever you need assistance. Feel free to ask another question.")

        conversation_count += 1

else:
    print("\nBot: Welcome!")
    print("Bot: Please start the conversation by typing Hello, Hi, or Hai.")